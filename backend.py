from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class Letters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    letter_id = db.Column(db.String(64), nullable=False)
    author = db.Column(db.String(16), nullable=False)
    text = db.Column(db.Text, nullable=False)
    recipient = db.Column(db.String(16), nullable=False)