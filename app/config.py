import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:pass123@localhost/movieman"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

