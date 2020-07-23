from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
import pandas as pd
from project.server import bcrypt, db
from project.server.models import User, BlacklistToken, Dataset
from project.server import utils

named_entity_recognition_blueprint = Blueprint('named_entity_recognition', __name__)


class NamedEntityRecognitionAPI(MethodView):
    def post(self):
        user = utils.get_user_from_header(request.headers)
        post_data = request.get_json()
        dataset = Dataset.query.filter_by(id=post_data["datasetId"], user_id=user.id).first()
        selected_column_name = post_data["column"]
        df = pd.read_csv(dataset.filepath)
        """
        TODO: Write your logic here.
        """
        df.to_csv(dataset.filepath, index=None)
        return jsonify(post_data)


named_entity_recognition_controller = NamedEntityRecognitionAPI.as_view('named_entity_recognition_api')

named_entity_recognition_blueprint.add_url_rule(
    '/ml/named_entity_recognition',
    view_func=named_entity_recognition_controller,
    methods=['POST']
)
