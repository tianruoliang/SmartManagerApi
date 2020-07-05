from app.plugin import db
from app.model.user import User


def get_user_list():
    data = User.query.all()
    return [d.to_dict() for d in data]


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
