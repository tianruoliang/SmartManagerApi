from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    jwt_required, jwt_refresh_token_required,
    get_jwt_identity, get_raw_jwt
)

from app.auth.helper import (
    is_token_revoked, add_token_to_database,
    revoke_token, remove_token
)
from app.model.user import User
from app.plugin import pwd_context, jwt

bp = Blueprint("auth", __name__, url_prefix="/smart-manager/auth")


@bp.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.query.filter_by(username=username).first()
    if user is None or not pwd_context.verify(password, user.password):
        return jsonify({"msg": "Bad credentials"}), 400

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    add_token_to_database(access_token, current_app.config["JWT_IDENTITY_CLAIM"])
    add_token_to_database(refresh_token, current_app.config["JWT_IDENTITY_CLAIM"])
    return jsonify(access_token=access_token, refresh_token=refresh_token)


@bp.route('/logout', methods=['POST'])
@jwt_required
def logout():
    """登出，清空所有token"""

    user_identity = get_jwt_identity()
    remove_token(user_identity)
    return jsonify({"msg": "logout"})


@bp.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    ret = {"access_token": access_token}
    add_token_to_database(access_token, current_app.config["JWT_IDENTITY_CLAIM"])
    return jsonify(ret)


@bp.route("/revoke_access", methods=["DELETE"])
@jwt_required
def revoke_access_token():
    jti = get_raw_jwt()["jti"]
    user_identity = get_jwt_identity()
    revoke_token(jti, user_identity)
    return jsonify({"msg": "token revoked"})


@bp.route("/revoke_refresh", methods=["DELETE"])
@jwt_refresh_token_required
def revoke_refresh_token():
    jti = get_raw_jwt()["jti"]
    user_identity = get_jwt_identity()
    revoke_token(jti, user_identity)
    return jsonify({"msg": "token revoked"})


@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    return User.query.get(identity)


@jwt.token_in_blacklist_loader
def check_if_token_revoked(decoded_token):
    return is_token_revoked(decoded_token)
