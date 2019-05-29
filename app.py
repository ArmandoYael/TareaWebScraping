# Import class Flask
from flask import Flask, jsonify, render_template
import pymongo
import requests

# Conexion a BD Mongo
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db

app = Flask(__name__)

@app.route("/scrape")
def scrape():

    from scrape_mars import scrape
    diccionario = scrape()
    db.general.drop() 
    db.general.insert_many(diccionario)
    return jsonify(scrape())

#Home
@app.route('/')
def home():
    mars_data = list(db.general.find())
    print(mars_data)
    return render_template("Index.html", dict=mars_data)

if __name__ == "__main__":
    app.run(debug=True)