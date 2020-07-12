import click
from flask.cli import AppGroup

from app.controller.user import create_user
from app.model.role import Role
from app.plugin import db

db_cli = AppGroup('db', help="Database client", short_help='List database script.')


@db_cli.command("init", short_help="Init all tables.")
def init_db():
    db.drop_all()
    db.create_all()
    Role.init_role()


@db_cli.command("faker", short_help="Faker test database.")
def faker_test_db():
    import random
    from app.model.company import Company
    from app.model.user import User

    db.drop_all()
    db.create_all()
    Role.init_role()

    admin_role = Role.query.filter_by(name="admin").first()
    admin = User(name="测试管理员",
                 username="admin",
                 password="123456",
                 phone="测试电话号码",
                 role_id=admin_role.id)
    db.session.add(admin)
    db.session.commit()

    companies = [Company(name="company-%d" % i,
                         address="address-%d" % i,
                         phone="phone-%d" % i,
                         c_type=random.choice(('供货商', '经销商'))) for i in range(10)]
    db.session.add_all(companies)
    db.session.commit()


@db_cli.command("create-admin", short_help="Add admin")
@click.argument('name')
@click.argument('username')
@click.argument('password')
def create_admin(name, username, password):
    admin_role = Role.query.filter_by(name="admin").first()
    create_user({
        "name": name,
        "username": username,
        "password": password,
        "role_id": admin_role.id
    })


def init_cli(app):
    app.cli.add_command(db_cli)
