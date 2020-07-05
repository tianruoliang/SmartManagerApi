from datetime import datetime

from app.plugin import db, pwd_context

ROLLS = ('admin', 'manager')


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    users = db.relationship('User', backref='role', lazy=True)

    @classmethod
    def init_role(cls):
        instance_list = [cls(name=name) for name in ROLLS]
        db.session.add_all(instance_list)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    account = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = pwd_context.hash(self.password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "phone": self.phone,
            "role": self.role.name,
            "create_time": self.create_time
        }
