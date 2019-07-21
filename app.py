from flask import Flask,render_template,jsonify,request
from flask_mysqldb import MySQL
app = Flask(__name__)
mysql = MySQL(app)

#Enter your database informations 
app.config["MYSQL_HOST"] = ""
app.config["MYSQL_USER"] = ""
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = ""
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/livesearch",methods=["POST","GET"])
def livesearch():
    searchbox = request.form.get('text')
    cursor = mysql.connection.cursor()
    query = "select word_eng from words where word_eng LIKE '{}%' order by word_eng".format(searchbox)#This is just exampel query , you should replace it with your query
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True)