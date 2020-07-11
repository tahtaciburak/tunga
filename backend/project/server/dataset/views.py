import os
import random
import json

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from werkzeug.utils import secure_filename

from project.server import bcrypt, db
from project.server.models import Dataset, User
from project.server import app

from project.server import utils
import pandas as pd
import pymongo
import subprocess

dataset_blueprint = Blueprint('dataset', __name__)


class DatasetManager:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.dataset_file_type = self.dataset_path.split(".")[-1]
        self.dataset = None
        self.delimiter = None
        self.analytics_result = {
            "n_rows": 0,
            "n_cols": 0,
            "n_missing_values": 0
        }
        self.columns = []
        self.df = None

    def create_dataframe(self):
        if self.dataset_file_type == "csv":
            return pd.read_csv(self.dataset_path)
        elif self.dataset_file_type == "xlsx" or self.dataset_file_type == "xls":
            return pd.read_excel(self.dataset_path)
        elif self.dataset_file_type == "json":
            return pd.read_json(self.dataset_file_type)
        elif self.dataset_file_type == "txt":
            with open(self.dataset_path, "r") as f:
                lines = pd.Series([item.strip() for item in f.readlines()])
            df_model = {
                "texts": lines
            }
            return pd.DataFrame(df_model)

    def analyze(self):
        df = self.create_dataframe()
        self.analytics_result["n_rows"] = df.shape[0]
        self.analytics_result["n_cols"] = df.shape[1]
        self.columns = df.columns
        self.df = df


class GetDatasetColumnNamesAPI(MethodView):
    def get(self, dataset_id):
        user = utils.get_user_from_header(request.headers)
        dataset = Dataset.query.filter_by(id=dataset_id).first()
        df = pd.read_csv(dataset.filepath)
        return jsonify({
            "dataset_id": dataset_id,
            "dataset_name": dataset.filename,
            "columns": list(df.columns)
        })


class GetUserDatasetsAPI(MethodView):
    """
    Bu method kullanıcın sahip olduğu bütün datasetleri getirir.
    """

    def get(self):
        user = utils.get_user_from_header(request.headers)
        user_datasets = []
        for ds in user.datasets:
            user_datasets.append(ds.as_dict())
        user_datasets = list(reversed(user_datasets))
        return make_response(jsonify({"datasets": user_datasets}))


class TwitterCrawlerAPI(MethodView):
    def post(self):
        user = utils.get_user_from_header(request.headers)
        return True


class RemoteFileFetchAPI(MethodView):
    def post(self):
        user = utils.get_user_from_header(request.headers)
        post_data = request.get_json()

        dataset_name = post_data["dataset_name"]
        dataset_description = post_data["dataset_description"]
        dataset_url = post_data["dataset_url"]
        file_name = dataset_url.split("/")[-1]
        upload_path = os.path.join(os.path.join(app.config['UPLOAD_PATH'], str(user.id)), file_name)
        a = subprocess.check_output(f"wget {dataset_url} -P {os.path.join(app.config['UPLOAD_PATH'], str(user.id))}",
                                    shell=True)

        dm = DatasetManager(upload_path)
        dm.analyze()

        records = json.loads(dm.df.T.to_json()).values()
        tungaclient = pymongo.MongoClient("mongodb://localhost:27017/")
        user_mongodb = tungaclient["db_" + str(user.id)]
        mycol = user_mongodb[dataset_name]
        mycol.insert(records)

        try:
            dataset = Dataset(
                filename=dataset_name,
                description=dataset_description,
                filepath=os.path.join(app.config['UPLOAD_PATH'], str(user.id)) + file_name,
                file_type=dm.dataset_file_type,
                size=0,  # TODO: fix here
                row_count=dm.analytics_result["n_rows"],
                user_id=user.id,
            )
            db.session.add(dataset)
            db.session.commit()
            responseObject = {
                'status': 'success',
                'message': 'Successfully uploaded.',
                'analytics': dm.analytics_result
            }

            return make_response(jsonify(responseObject)), 201

        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObject)), 400


class LocalUploadAPI(MethodView):
    def post(self):
        user = utils.get_user_from_header(request.headers)

        file = request.files["file"]
        file_name = secure_filename(utils.generate_file_name(file.filename))

        utils.create_user_upload_path_if_not_exists(app.config['UPLOAD_PATH'], str(user.id))
        upload_path = os.path.abspath(os.path.join(app.config['UPLOAD_PATH'], str(user.id), file_name))

        file_type = file.filename.rsplit('.', 1)[1].lower()
        file_owner_id = user.id
        dataset_name = request.form["dataset_name"]
        dataset_description = request.form["dataset_description"]
        file.save(upload_path)
        n_rows = 0
        n_cols = 0
        n_missing_values = 0
        if file_type == "csv":
            try:
                df = pd.read_csv(upload_path)
                n_rows = df.shape[0]
                n_cols = df.shape[1]
                n_missing_values = 0  # df.isnull().sum()
            except:
                return make_response(jsonify({
                    "status": 'error',
                    "reason": "improper csv file"
                })), 401
        elif file_type == "txt":
            with open(upload_path, "r") as f:
                lines = pd.Series([item.strip() for item in f.readlines()])
            df_model = {
                "texts": lines
            }
            df = pd.DataFrame(df_model)
            n_rows = df.shape[0]
            n_cols = df.shape[1]
            n_missing_values = df.isnull().sum()
        elif file_type == "xlsx":
            try:
                df = pd.read_excel(upload_path)
                n_rows = df.shape[0]
                n_cols = df.shape[1]
                n_missing_values = df.isnull().sum()
            except:
                return make_response(jsonify({
                    "status": 'error',
                    "reason": "improper excel file"
                })), 401
        elif file_type == "json":
            try:
                df = pd.read_json(upload_path)
                n_rows = df.shape[0]
                n_cols = df.shape[1]
                n_missing_values = df.isnull().sum()
            except:
                return make_response(jsonify({
                    "status": 'error',
                    "reason": "improper json file"
                })), 401
        else:
            return make_response(jsonify({
                "status": 'error',
                "reason": "unknown file type"
            })), 401

        records = json.loads(df.T.to_json()).values()
        tungaclient = pymongo.MongoClient("mongodb://localhost:27017/")
        user_mongodb = tungaclient["db_" + str(user.id)]
        mycol = user_mongodb[dataset_name]
        mycol.insert(records)
        try:
            dataset = Dataset(
                filename=dataset_name,
                description=dataset_description,
                filepath=upload_path,
                size=0,  # TODO: fix here
                row_count=n_rows,
                user_id=file_owner_id,
                file_type=file_type
            )
            db.session.add(dataset)
            db.session.commit()
            responseObject = {
                'status': 'success',
                'message': 'Successfully uploaded.',
                'analytics': {
                    'nrows': int(n_rows),
                    'ncols': int(n_cols),
                    'n_missing_values': int(n_missing_values)
                }
            }

            return make_response(jsonify(responseObject)), 201

        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return make_response(jsonify(responseObject)), 401


local_dataset_upload_view = LocalUploadAPI.as_view('local_dataset_upload_api')
remote_dataset_upload_view = RemoteFileFetchAPI.as_view('remote_dataset_upload_api')
get_user_datasets = GetUserDatasetsAPI.as_view('get_user_datasets_api')
get_dataset_column_names = GetDatasetColumnNamesAPI.as_view('get_dataset_column_names_api')

dataset_blueprint.add_url_rule(
    '/dataset/<dataset_id>/columns',
    view_func=get_dataset_column_names,
    methods=['GET']
)

dataset_blueprint.add_url_rule(
    '/dataset/local',
    view_func=local_dataset_upload_view,
    methods=['POST']
)

dataset_blueprint.add_url_rule(
    '/dataset/remote',
    view_func=remote_dataset_upload_view,
    methods=['POST']
)

dataset_blueprint.add_url_rule(
    '/dataset/all',
    view_func=get_user_datasets,
    methods=['GET']
)
