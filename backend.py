from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from hashlib import sha256

from sqlalchemy import desc

app = Flask(__name__)
db = SQLAlchemy(app)


class Letters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    letter_id = db.Column(db.String(64), nullable=False)
    author = db.Column(db.String(16), nullable=False)
    text = db.Column(db.Text, nullable=False)
    recipient = db.Column(db.String(16), nullable=False)


# method adding data to database
def add_letter_to_database(letter_id, author, text, recipient):
    data = Letters(letter_id=letter_id, author=author, text=text, recipient=recipient)
    try:
        db.session.add(data)
        db.session.commit()
    except:
        return redirect('index.html')


# method getting number of letter in database
def get_letter_id_from_db():
    last_id = Letters.query.order_by(desc(Letters.id)).first().id
    return int(last_id) + 1


# method of creating a unique ID by encryption method
def create_unique_id(letter_id):
    return sha256(letter_id.encode('utf-8')).hexdigest()


