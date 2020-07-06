from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scraper

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/martian_app'
mongo = PyMongo(app)
print('1st step complete')

@app.route('/')
def index():
    print('2nd step complete')
    mars_to_mongo = list(mongo.db.martian_db.find())
    return render_template('index.html', mars_to_html = mars_to_mongo)

@app.route('/scrape')
def scraper():
    print('3rd step complete')
    mars_data_from_mongo = mongo.db.martian_db
    mars_data_from_mongo.drop()
    scraped_mars_data = mars_scraper.scrape()
    mars_data_from_mongo.update({}, scraped_mars_data, upsert = True)
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run( debug = True )
