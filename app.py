from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL(app)

#Enter here your database informations 
app.config["MYSQL_HOST"] = ""
app.config["MYSQL_USER"] = ""
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = ""
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/livesearch", methods=["POST","GET"])
def livesearch():
    data = request.get_json(force=True)
    searchbox = data["text"]

    cursor = mysql.connection.cursor()
    query = f"SELECT word_eng FROM words WHERE word_eng LIKE '{searchbox}%' ORDER BY word_eng" #This is just example query , you should replace field names with yours
    cursor.execute(query)
    result = cursor.fetchall() #Ordinarily cursor.fetchall() returns a tuple but because we specified the
                               #CursorClass, a dict is returned and it is easily 'jsonified'

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)