# -*- coding: utf-8 -*-

from contextlib import contextmanager

from sqlalchemy import any_, create_engine
from sqlalchemy.orm import sessionmaker

from model import BusinessCard


class Dao:
    def __init__(self):
        self.engine = create_engine(
            'mysql://root:pass@172.16.238.20/evo_db?charset=utf8', echo=True
        )
        self.Session = sessionmaker(bind=self.engine)

    def select_all_business_cards(self):
        session = self.Session()
        return session.query(BusinessCard)

    def select_business_cards_by_name(self, word):
        session = self.Session()
        return session.query(BusinessCard).filter(
            BusinessCard.name.like(f'%{word}%'))

    def select_business_cards_by_company(self, word):
        session = self.Session()
        return session.query(BusinessCard).filter(
            BusinessCard.company.in_(word.split()))

    def select_business_cards_by_tel(self, word):
        session = self.Session()
        return session.query(BusinessCard).filter(BusinessCard.tel == word)

    def select_business_cards_by_mail(self, word):
        session = self.Session()
        return session.query(BusinessCard).filter(BusinessCard.mail == word)

    def insert_business_card(self, kwargs):
        with self.open_session() as session:
            session.add(BusinessCard(**kwargs))

    @contextmanager
    def open_session(self):
        session = self.Session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
