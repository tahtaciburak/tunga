from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
import pandas as pd

from project.server import db
from project.server.models import Configuration, Dataset
from project.server import utils

preprocessing_blueprint = Blueprint('preprocessing', __name__)


class PreprocessingControllerAPI(MethodView):
    def post(self):
        user = utils.get_user_from_header(request.headers)
        post_data = request.get_json()
        dataset = Dataset.query.filter_by(id=post_data["datasetId"], user_id=user.id).first()
        selected_column_name = post_data["column"]
        df = pd.read_csv(dataset.filepath)
        df["PREPROCESSED_" + selected_column_name] = pd.Series([str(item).upper() for item in df[selected_column_name]])
        df.to_csv(dataset.filepath, index=None)
        return jsonify(post_data)


preprocessing_controller = PreprocessingControllerAPI.as_view('preprocessing_controller_api')

preprocessing_blueprint.add_url_rule(
    '/preprocessing',
    view_func=preprocessing_controller,
    methods=['POST']
)
