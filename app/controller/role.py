from app.model.role import Role


def get_role_list():
    return Role.query.all()
