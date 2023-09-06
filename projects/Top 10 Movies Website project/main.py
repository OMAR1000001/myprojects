from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class bestmoves(FlaskForm):
    movie_title=StringField('title',validators=[DataRequired()])
    movie_year=StringField('year',validators=[DataRequired()])
    movie_description=StringField('description',validators=[DataRequired()])
    movie_rating=StringField('rating',validators=[DataRequired()])
    movie_ranking=StringField('ranking',validators=[DataRequired()])
    movie_review=StringField('review',validators=[DataRequired()])
    movie_img_url=StringField('img url',validators=[DataRequired()])
    submit=SubmitField("submit")

class edit_form(FlaskForm):
    rate=StringField('rate',validators=[DataRequired()])
    title=StringField('title',validators=[DataRequired()])
    submit=SubmitField("submit")

class delete(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    submit = SubmitField("submit")


    connection = sqlite3.connect("top_movies.db")
    cursor = connection.cursor()
    try:
        cursor.execute(
            "CREATE TABLE movie(title TEXT,year TEXT,description TEXT,rating TEXT,ranking TEXT,review TEXT,img_url TEXT )")
    except:
        pass
    all_moves = cursor.execute("SELECT * FROM movie").fetchall()

@app.route("/")
def home():
    connection = sqlite3.connect("top_movies.db")
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE TABLE movie(title TEXT,year TEXT,description TEXT,rating TEXT,ranking TEXT,review TEXT,img_url TEXT )")
    except:
        pass
    all_moves = cursor.execute("SELECT * FROM movie").fetchall()
    num=len(all_moves)

    return render_template("index.html",all_moves=all_moves,num=num)

@app.route("/add", methods=['GET', 'POST'])
def add():
    connection = sqlite3.connect("top_movies.db")
    cursor = connection.cursor()

    try:
        cursor.execute("CREATE TABLE movie(title TEXT,year TEXT,description TEXT,rating TEXT,ranking TEXT,review TEXT,img_url TEXT )")
    except:
        pass

    all_moves = cursor.execute("SELECT * FROM movie").fetchall()

    form=bestmoves()

    if form.validate_on_submit() and request.method == 'POST':
        if len(all_moves)<10 :

            title=f"{form.movie_title.data}"
            year = f"{form.movie_year.data}"
            description = f"{form.movie_description.data}"
            rating = f"{form.movie_rating.data}"
            ranking=f"{form.movie_ranking.data}"
            review=f"{form.movie_review.data}"
            img_url = f"{form.movie_img_url.data}"

            cursor.execute(f"INSERT INTO movie VALUES ('{title}', '{year}', '{description}', '{rating}', '{ranking}', '{review}', '{img_url}')")
            connection.commit()
            all_moves = cursor.execute("SELECT * FROM movie").fetchall()
            print(all_moves)
            return redirect("/")

    cursor.close()
    return render_template('add.html', form=form)

@app.route('/edit',methods=['GET','POST'])
def edit():
    connection = sqlite3.connect("top_movies.db")
    cursor = connection.cursor()

    try:
        cursor.execute("CREATE TABLE movie(title TEXT,year TEXT,description TEXT,rating TEXT,ranking TEXT,review TEXT,img_url TEXT )")
    except:
        pass
    rate_form=edit_form()
    if rate_form.validate_on_submit() and request.method =='POST':
        rate1=f'{rate_form.rate.data}'
        title2=f'{rate_form.title.data}'
        cursor.execute("UPDATE movie SET rating = ? WHERE title = ?", (rate1, title2))
        connection.commit()
        all_moves = cursor.execute("SELECT * FROM movie").fetchall()
        print(all_moves)
        return redirect("/")

    cursor.close()
    return render_template('edit.html', form=rate_form)

@app.route('/delete',methods=['GET','POST'])
def delete():
    connection = sqlite3.connect("top_movies.db")
    cursor = connection.cursor()
    deleteM=delete()
    if deleteM.validate_on_submit() and request.method =='POST':
        title2=f'{deleteM.title.data}'
        cursor.execute("DELETE FROM movie WHERE name = ?", (title2,))
        connection.commit()
        all_moves = cursor.execute("SELECT * FROM movie").fetchall()
        print(all_moves)
        return redirect("/")

    cursor.close()
    return render_template('select.html', form=deleteM)








if __name__ == '__main__':
    app.run(debug=True)
