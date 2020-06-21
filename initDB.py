from app import app
from model import db


db.create_all(app=app)
