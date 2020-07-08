import os
import random

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from werkzeug.utils import secure_filename

from project.server import bcrypt, db
from project.server.models import Dataset, User
from project.server import app

from project.server import utils
import pandas as pd

dataset_blueprint = Blueprint('dataset', __name__)


class GetUserDatasetsAPI(MethodView):
    def get(self):
        user = utils.get_user_from_header(request.headers)
        dss = []
        for ds in user.datasets:
            dss.append(ds.as_dict())
        dss = list(reversed(dss))
        return make_response(jsonify({"datasets": dss}))


class TwitterCrawlerAPI(MethodView):
    def post(self):
        user = utils.get_user_from_header(request.headers)
        return True


class RemoteFileFetchAPI(MethodView):
    def post(self):
        user = utils.get_user_from_header(request.headers)
        pass


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
                n_rows = int(df.shape[0])
                n_cols = df.shape[1]
                n_missing_values = 0#df.isnull().sum()
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
        try:
            dataset = Dataset(
                filename=dataset_name,
                description=dataset_description,
                filepath=upload_path,
                size=0,  # TODO: fix here
                row_count=len(file.readlines()),
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
get_user_datasets = GetUserDatasetsAPI.as_view('get_user_datasets_api')

dataset_blueprint.add_url_rule(
    '/dataset/local',
    view_func=local_dataset_upload_view,
    methods=['POST']
)

dataset_blueprint.add_url_rule(
    '/dataset/all',
    view_func=get_user_datasets,
    methods=['GET']
)
