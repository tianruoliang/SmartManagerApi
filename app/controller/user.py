from app.model.user import User
from app.plugin import db


def get_user_list():
    return User.query.all()


def get_user_detail(uid):
    return User.query.get_or_404(uid)


def create_user(info):
    user = User(**info)
    db.session.add(user)
    db.session.commit()
    return user


def delete_user(uid):
    user = User.query.get_or_404(uid)
    db.session.delete(user)
    db.session.commit()
    return user
