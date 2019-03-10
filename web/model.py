# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# 名刺テーブルのモデルクラス
class BusinessCard(Base):
    __tablename__ = 'business_card'
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    company = Column(String(32))
    tel = Column(String(16))
    mail = Column(String(32))
