import os
import random

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import Dataset, User
from project.server import app

from project.server import utils

dataset_blueprint = Blueprint('dataset', __name__)


class GetUserDatasetsAPI(MethodView):
    def get(self):
        user = utils.get_user_from_header(request.headers)
        print(user.datasets)
        dss = []
        for ds in user.datasets:
            dss.append(ds.as_dict())
        return make_response(jsonify({"datasets": dss}))


class LocalUploadAPI(MethodView):
    def post(self):
        user = utils.get_user_from_header(request.headers)

        file = request.files["file"]
        file_name = file.filename.split(".")[0] + "_" + str(random.randint(10000, 99999)) + "." + \
                    file.filename.split(".")[1]
        upload_path = os.path.abspath(os.path.join(app.config['UPLOAD_PATH'], file_name))

        file_owner_id = user.id
        dataset_name = request.form["dataset_name"]
        dataset_description = request.form["dataset_description"]

        file.save(upload_path)

        try:
            dataset = Dataset(
                filename=dataset_name,
                description=dataset_description,
                filepath=upload_path,
                size=0,  # TODO: fix here
                row_count=0,  # TODO: fix here
                user_id=file_owner_id
            )
            db.session.add(dataset)
            db.session.commit()
            responseObject = {
                'status': 'success',
                'message': 'Successfully uploaded.',
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
