from sqlalchemy import Column, Integer, Text, VARCHAR, DateTime
from models.datebase import Base
from datetime import datetime
from sqlalchemy.schema import ForeignKey

"""テーブルのカラム情報を定義するためのクラスを格納する"""
"""テーブル操作を行う際のレコード生成もこのクラスを通して行う"""

"""クラスとテーブルは1対1に対応している"""
"""クラス名は何でもOK"""
class user(BASE):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(Text, nullable=False)
    room_number = Column(Text, nullable=False)
    hash = Column(VARCHAR, nullable=False)

class product(BASE):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id  = Column(Integer, ForeignKey("user.id", nullable=False))
    title = Column(Text, nullable=False)
    body  = Column(Text, nullable=False)
    picture_path  = Column(Text, nullable=False)
    date = Column(DateTime, default=datetime.now())