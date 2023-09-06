from flask import Flask,render_template,request,jsonify
from fastapi import FastAPI
from uuid import uuid4
import sqlite3
import random



app=Flask(__name__)

connaction=sqlite3.connect("cafes.db")
curser=connaction.cursor()


caffes=curser.execute("SELECT * FROM cafe").fetchall()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/all")
def all():
    return jsonify(caffes)

@app.route("/random")
def random_cofe():
    return jsonify(random.choice(caffes))

@app.route("/search")
def search():
    req_loc=request.args.get('loc')
    search_name= f"'{req_loc}'"
    if search_name:
        connaction = sqlite3.connect("cafes.db")
        curser = connaction.cursor()
        caffes_info = curser.execute(f"SELECT * FROM cafe WHERE (location={search_name})").fetchall()
        if caffes_info ==[]:
            return jsonify({'stats': 'not found'}),404
        return jsonify(caffes_info)
    else:
        return jsonify({'stats': 'not found'}) ,404


@app.route("/add",methods=["POST"])
def post():
    connaction = sqlite3.connect("cafes.db")
    curser = connaction.cursor()
    curser.execute(f'INSERT INTO cafe VALUES ("{request.form.get("id")}","{request.form.get("name")}","{request.form.get("map_url")}","{request.form.get("img_url")}","{request.form.get("loc")}",'
                   f'"{bool(request.form.get("sockets"))}","{bool(request.form.get("toilet"))}","{bool(request.form.get("wifi"))}",'
                   f'"{bool(request.form.get("calls"))}","{request.form.get("seats")}","{request.form.get("coffee_price")}")').fetchall()

    # curser.execute(f'INSERT INTO cafe VALUES ({request.form.get("id")},{request.form.get("name")},{request.form.get("map_url")},'
    #                           f'{request.form.get("img_url")},{request.form.get("loc")},{bool(request.form.get("sockets"))},{bool(request.form.get("toilet"))},'
    #                           f'{bool(request.form.get("wifi"))},{bool(request.form.get("calls"))},{request.form.get("seats")},{request.form.get("coffee_price")})').fetchall()
    connaction.commit()
    curser.close()
    return jsonify({"success": "Successfully added the new cafe."})

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch(cafe_id):
    new_price=request.args.get("new_price")
    connaction = sqlite3.connect("cafes.db")
    curser = connaction.cursor()
    id=curser.execute("SELECT * FROM cafe WHERE id = ?",(f'{cafe_id}',),).fetchall()
    if id and request.method == "PATCH" :
        curser.execute(f'UPDATE cafe SET coffee_price = ? WHERE id = ?',(f"{cafe_id}",f"{new_price}")).fetchall()
        caffes = curser.execute("SELECT * FROM cafe").fetchall()
        print(caffes)
        connaction.commit()
        caffes = curser.execute("SELECT * FROM cafe").fetchall()
        print(caffes)
        return jsonify({"success": "Successfully added the new cafe."}) ,200
    else:
        return jsonify({"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

@app.route('/report-closed/<int:cafe_id>',methods=["DELETE"])
def delete(cafe_id):
    api_key=request.args.get("api-key")
    connaction = sqlite3.connect("cafes.db")
    curser = connaction.cursor()
    id=curser.execute('SELECT id FROM cafe WHERE id = ?',(cafe_id,),).fetchall()
    connaction.commit()
    if api_key == 'TopSecretAPIKey' :
        if id :
            curser.execute('DELETE FROM cafe WHERE id = ?', (f"{cafe_id}",))
            connaction.commit()
            return jsonify({"success": "Successfully deleted the cafe from the database."}), 200

        else:
            return jsonify({"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify({"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403




if __name__ == '__main__':
    app.run(debug=True)