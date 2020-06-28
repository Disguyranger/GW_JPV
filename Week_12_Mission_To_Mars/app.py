from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_m

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mData = list(mongo.db.mData.find())
    return render_template("index.html", mData=mData)

@app.route("/scrape")
def scraper():
    mData = mongo.db.mData
    mData.drop()
    mData_scraped = scrape_m.scrape()
    mData.insert_many(mData_data)
    return redirect("/", code=302)
if __name__ == "__main__":
    app.run(debug=True)