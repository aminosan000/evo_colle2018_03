# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BusinessCard(Base):
    __tablename__ = 'business_card'
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    company = Column(String(32))
    tel = Column(String(16))
    mail = Column(String(32))
    user_id = Column(String(32))


class User(Base):
    __tablename__ = 'user'
    user_id = Column(String(32), primary_key=True)
    password = Column(String(256))
