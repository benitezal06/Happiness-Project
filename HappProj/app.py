from flask import Flask, render_template
import pymongo
from bson.json_util import dumps
import os
import json

app = Flask(__name__)

# added 5/21 debug
app.config['DEBUG'] = True

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.ranking_happiness
happiness = db.happiness
geoJsonCountry = db.geoJsonCountry

# Show map with countries colored by rank
@app.route("/api/v1/getGeoJsonData/<year>")
def getGeoJsonData(year):

    print ("at getGeoJsonData..." + str(year))

    if year.isnumeric():
        records = list(geoJsonCountry.find({"dataYear": int(year)}))
    else:
        records = list(geoJsonCountry.find({}))

    if records:
        print("records found: " + str(len(records)))
    else:
        print("no data found!")

    return dumps(records)


@app.route("/api/v1/alldata")
def happ():

    print ("at happ...")
    # write a statement that finds all the items in the db and sets it to a variable
    records = list(db.happiness.find())
    #print(records)

    # render an index.html template and pass it the data you retrieved from the database
    return dumps(records)

# Returns years - used in filter drop down
@app.route("/getYears")
def getYears():
    print ("at getYears...")
    records = list(db.happiness.distinct( "Data_Year" ))
    return dumps(records)

@app.route("/")
def main():
    print ("at root...")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


