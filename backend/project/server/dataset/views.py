import os
import random

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import Dataset, User
from project.server import app

dataset_blueprint = Blueprint('dataset', __name__)


class UploadAPI(MethodView):
    """
    User Registration Resource
    """

    def post(self):
        post_data = request.get_json()
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
                resp = User.decode_auth_token(auth_token)
                if not isinstance(resp,str):
                    user = User.query.filter_by(id=resp).first()
                    file = request.files["file"]
                    file_name = file.filename.split(".")[0] + "_" + str(random.randint(10000, 99999)) + "." + \
                                file.filename.split(".")[1]
                    upload_path = os.path.abspath(os.path.join(app.config['UPLOAD_PATH'], file_name))
                    file_owner_id = user.id
                    file_description = request.form["description"]
                    file.save(upload_path)

                    try:
                        dataset = Dataset(
                            filename=file_name,
                            description=file_description,
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


            except IndexError:
                response_object = {
                    'status': 'fail',
                    'message': 'Bearer token malformed'
                }
                return make_response(jsonify(response_object))



# define the API resources
upload_view = UploadAPI.as_view('upload_api')

# add Rules for API Endpoints
dataset_blueprint.add_url_rule(
    '/dataset/upload',
    view_func=upload_view,
    methods=['POST']
)
