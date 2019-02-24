# -*- coding: utf-8 -*-

from sqlalchemy_utils import database_exists, create_database
from werkzeug.security import generate_password_hash

from model import User, Base
from dao import Dao


def setup_db():
    dao = Dao()
    engine = dao.engine
    session = dao.session

    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)
    password_hash = generate_password_hash('admin')
    session.add(User(user_id='admin', password=password_hash))


if __name__ == '__main__':
    setup_db()
