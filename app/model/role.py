from app.plugin import db

ROLLS = ('admin', 'common')


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    users = db.relationship('User', backref='role', lazy='joined')

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
