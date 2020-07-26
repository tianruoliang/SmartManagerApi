from app.model.user import User
from app.plugin import db


def get_user_list():
    return [u.to_dict() for u in  User.query.all()]


def get_user_detail(uid):
    user = User.query.get_or_404(uid)
    return user.to_dict()


def create_user(info):
    user = User(**info)
    db.session.add(user)
    db.session.commit()
    return user.to_dict()


def delete_user(uid):
    user = User.query.get_or_404(uid)
    db.session.delete(user)
    db.session.commit()
    return user.to_dict()
