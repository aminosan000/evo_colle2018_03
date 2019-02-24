# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import BusinessCard, User


class Dao:
    def __init__(self):
        self.engine = create_engine(
            'mysql://root:pass@172.16.238.20/evo_db?charset=utf8', echo=True
        )

        Session = sessionmaker(bind=self.engine, autocommit=True)
        self.session = Session()

    def select_user(self, user_id):
        return self.session.query(User).get(user_id)

    def select_business_cards(self, user_id):
        return self.session.query(BusinessCard).filter_by(user_id=user_id)

    def insert_business_card(self, kwargs):
        self.session.add(BusinessCard(**kwargs))
