from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import db
from project.server.models import Configuration
from project.server import utils

preprocessing_blueprint = Blueprint('preprocessing', __name__)


class PreprocessingControllerAPI(MethodView):
    def post(self):
        user = utils.get_user_from_header(request.headers)
        post_data = request.get_json()
        print(post_data)
        return jsonify(post_data)

preprocessing_controller = PreprocessingControllerAPI.as_view('preprocessing_controller_api')

preprocessing_blueprint.add_url_rule(
    '/preprocessing',
    view_func=preprocessing_controller,
    methods=['POST']
)
