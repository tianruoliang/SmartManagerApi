from app.model.role import Role


def get_role_list():
    data = Role.query.all()
    return [d.to_dict() for d in data]
