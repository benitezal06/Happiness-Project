from flask import Flask, render_template
import pymongo
from bson.json_util import dumps

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.ranking_happiness
happiness = db.happiness


@app.route("/api/v1/alldata")
def happ():
    # write a statement that finds all the items in the db and sets it to a variable
    records = list(db.happiness.find())
    print(records)

    # render an index.html template and pass it the data you retrieved from the database
    return dumps(records)

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


