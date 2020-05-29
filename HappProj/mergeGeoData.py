# downloaded the geoJson file from http://geojson.xyz/
#    >> admin 0 countries	110	149 polygons	602.55 kB	political_countries
# used in adding the polygon in the map based on country happiness rank
# renamed the file to countries.geojson under static\data folder.

import pymongo
import os
import json

# Setup connection to mongodb
conn = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.ranking_happiness

happiness = db.happiness
geoJsonCountry = db.geoJsonCountry

# Clear any existing data in geoJsonCountry
geoJsonCountry.drop()

# Populate geoJsonCountry collection
print("Merging geoJson data with World Happiness Data...")
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "static/data", "countries.geojson")
geoJsonCountryData = json.load(open(json_url))

# geoJsonTextFile = []

# Merge
for geoCntry in geoJsonCountryData["features"]:
    geometry = geoCntry["geometry"]
    prop = geoCntry["properties"]
    countryName = prop["name"]

    # Loop for each year
    for year in happiness.distinct( "Data_Year" ):
        # print(year)

        # Loop through happiness collection for the country and the year
        happinessData = happiness.find({ "Data_Year": year, "Country": countryName}, {"_id": 0})
        # print(str(year))
        if happinessData:
            geojson = {
            "type": "FeatureCollection",
            "dataYear": year,
            "dataCountry": countryName,
            "features": [
            {
                "type": "Feature",
                "geometry" : geometry,
                "properties" : d,
            } for d in happinessData]}
            # print (geojson)
            geoJsonCountry.insert_one(geojson)
            # geoJsonTextFile.append(geojson)
        else:
            print("country not found: " + countryName)

# For testing - create the geo json file
# with open('geoJsonTestFile.json', 'w') as f:
#     json.dump(geojson, f)

print(str(geoJsonCountry.count_documents({})) + " records created.")
print("done...")



