from sqlalchemy import Column, Integer, Text, VARCHAR, DateTime
from models.datebase import Base
from datetime import datetime

"""テーブルのカラム情報を定義するためのクラスを格納する"""
"""テーブル操作を行う際のレコード生成もこのクラスを通して行う"""

class user(BASE):