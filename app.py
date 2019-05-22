from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mission")


@app.route("/")
def home():
    mission_data = mongo.db.mars.find_one()
    return render_template("index.html", data=mission_data)


@app.route('/scrape')
def scrape():
    mars = scrape_mars.scrape()
    print("\n\n\n")

    mongo.db.mars.update({}, mars, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
