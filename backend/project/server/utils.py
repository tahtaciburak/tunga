from project.server.models import User


def get_user_from_header(header_data):
    auth_header = header_data.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
        resp = User.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            user = User.query.filter_by(id=resp).first()
            return user
    return None
