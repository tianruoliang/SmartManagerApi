from datetime import datetime

from flask_jwt_extended import decode_token
from sqlalchemy.orm.exc import NoResultFound, ObjectDeletedError

from app.model.token import TokenAllowList
from app.plugin import db


def add_token_to_database(encoded_token, identity_claim):
    decoded_token = decode_token(encoded_token)
    jti = decoded_token["jti"]
    token_type = decoded_token["type"]
    user_identity = decoded_token[identity_claim]
    expires = datetime.fromtimestamp(decoded_token["exp"])
    revoked = False

    db_token = TokenAllowList(
        jti=jti,
        token_type=token_type,
        user_id=user_identity,
        expires=expires,
        revoked=revoked,
    )
    db.session.add(db_token)
    db.session.commit()


def is_token_revoked(decoded_token):
    jti = decoded_token["jti"]
    try:
        token = TokenAllowList.query.filter_by(jti=jti).one()
        return token.revoked
    except NoResultFound:
        return True


def revoke_token(token_jti, user_id):
    try:
        token = TokenAllowList.query.filter_by(jti=token_jti, user_id=user_id).one()
        token.revoked = True
        db.session.commit()
    except NoResultFound:
        raise Exception("Could not find the token {}".format(token_jti))


def remove_token(user_id):
    try:
        TokenAllowList.query.filter_by(user_id=user_id).delete()
        db.session.commit()
    except ObjectDeletedError:
        raise Exception("Could not delete token by {}".format(user_id))
