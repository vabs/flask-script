import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///home/reviews.db")
db = SQLAlchemy(app)

class StatsData(db.Model):
	__tablename__ = 'statsdata'
	stats_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	token_id = db.Column(db.String)
	location_name = db.Column(db.String)
	listing_count = db.Column(db.BigInteger)
	reviews_count = db.Column(db.BigInteger)
	start_date = db.Column(db.Date)
	last_updated_date = db.Column(db.Date)