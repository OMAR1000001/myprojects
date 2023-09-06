from flask import Flask, render_template,request,redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,URLField,SelectField
from wtforms.validators import DataRequired
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY']='8BYkEfBA6O6donzWlSihBXox7C0sKR6b0'
Bootstrap(app)
class formclass(FlaskForm):
    book_name=StringField('title',validators=[DataRequired()])
    book_authar=StringField('auther',validators=[DataRequired()])
    book_rating=SelectField('rating',choices=[1,2,3,4,5],validators=[DataRequired()])
    submit=SubmitField('Submit')

connection=sqlite3.connect("library_books.db")
cursor=connection.cursor()

try:
    cursor.execute("CREATE TABLE library(title TEXT,auther TEXT,rating INTEGER )")
except:
    pass

all_books=cursor.execute("SELECT * FROM library").fetchall()


@app.route('/')
def home():

    connection = sqlite3.connect("library_books.db")
    cursor = connection.cursor()

    try:
        cursor.execute("CREATE TABLE library(title TEXT,auther TEXT,rating INTEGER )")
    except:
        pass

    all_books = cursor.execute("SELECT * FROM library").fetchall()

    print(f" ------------------------------ {all_books} ------------------------------------ ")
    return render_template('index.html',all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    connection = sqlite3.connect("library_books.db")
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE TABLE library(title TEXT,auther TEXT,rating INTEGER )")
    except:
        pass

    all_books = cursor.execute("SELECT title, auther, rating FROM library").fetchall()
    form=formclass()

    if form.validate_on_submit() and request.method == "POST":
        name=f"{form.book_name.data}"
        auther=f"{form.book_authar.data}"
        rating=f"{form.book_rating.data}"
        cursor.execute(f"INSERT INTO library VALUES ('{name}', '{auther}', {rating})")
        connection.commit()
        all_books = cursor.execute("SELECT * FROM library").fetchall()
        print(all_books)
        # cursor.close()
        return redirect("/")



    return render_template('add.html',form=form)

# @app.route("/add",methods=['GET','POST'])
# def add():
#     form=formclass()
#     if form.validate_on_submit() and request.method == "POST":
#         title = request.form["title"]
#         author = request.form["author"]
#         rating = request.form["rating"]
#         cursor.execute(f"INSERT INTO fish VALUES ('{title}', '{author}', {rating})")
#         return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

