from flask import Flask, render_template, request, redirect
from secret import secretkey
from flask_sqlalchemy import SQLAlchemy
from backend import create_unique_id, add_letter_to_database, get_letter_id_from_db, get_letter_by_unique_letter_id

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = secretkey
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# main page
@app.route('/', methods=["POST", "GET"])
def create_letter():
    if request.method == "POST":
        letter_id = create_unique_id(str(get_letter_id_from_db()))  # Create unique id like e7f6c011776e8... basic on number id in database
        author = request.form.get('author')
        text = request.form.get('text')
        recipient = request.form.get('recipient')
        add_letter_to_database(letter_id, author, text, recipient)  # Add letter with all content in db
        return redirect(f'http://127.0.0.1:5000/letter/{letter_id}')
    return render_template('index.html')


# Letter page
@app.route('/letter/<string:letter_id>')
def letter(letter_id):
    letter_content = get_letter_by_unique_letter_id(letter_id)
    return render_template('letter.html', content=letter_content)


if __name__ == '__main__':
    app.run()
