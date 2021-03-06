import pymongo
import bson
from bson.raw_bson import RawBSONDocument
from bson.codec_options import CodecOptions

# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.ranking_happiness
db.happiness.drop()
happiness = db.happiness


happiness.insert_many([
  {
    "Country": "Afghanistan",
    "Data_Year": 2018,
    "Happiness_Rank": 145,
    "Happiness_Score": 3.63,
    "Life_Expectancy": 63.7,
    "Population": 37200000,
    "Latitude": 33.93911,
    "Longitude": 67.709953
  },
  {
    "Country": "Afghanistan",
    "Data_Year": 2017,
    "Happiness_Rank": 141,
    "Happiness_Score": 3.79,
    "Life_Expectancy": 63.4,
    "Population": 36300000,
    "Latitude": 33.93911,
    "Longitude": 67.709953
  },
  {
    "Country": "Afghanistan",
    "Data_Year": 2016,
    "Happiness_Rank": 154,
    "Happiness_Score": 3.36,
    "Life_Expectancy": 61.2,
    "Population": 35400000,
    "Latitude": 33.93911,
    "Longitude": 67.709953
  },
  {
    "Country": "Afghanistan",
    "Data_Year": 2015,
    "Happiness_Rank": 153,
    "Happiness_Score": 3.58,
    "Life_Expectancy": 61.2,
    "Population": 34400000,
    "Latitude": 33.93911,
    "Longitude": 67.709953
  },
  {
    "Country": "Singapore",
    "Data_Year": 2019,
    "Happiness_Rank": 34,
    "Happiness_Score": 6.34,
    "Life_Expectancy": 85.1,
    "Population": 5800000,
    "Latitude": 1.352083,
    "Longitude": 103.819836
  },
  {
    "Country": "Albania",
    "Data_Year": 2017,
    "Happiness_Rank": 109,
    "Happiness_Score": 4.64,
    "Life_Expectancy": 78.2,
    "Population": 2880000,
    "Latitude": 41.153332,
    "Longitude": 20.168331
  },
  {
    "Country": "Hong Kong",
    "Data_Year": 2019,
    "Happiness_Rank": 76,
    "Happiness_Score": 5.43,
    "Life_Expectancy": 84.76,
    "Population": 7436154,
    "Latitude": 22.3193,
    "Longitude": 114.1694
  },
  {
    "Country": "Albania",
    "Data_Year": 2015,
    "Happiness_Rank": 95,
    "Happiness_Score": 4.96,
    "Life_Expectancy": 78,
    "Population": 2890000,
    "Latitude": 41.153332,
    "Longitude": 20.168331
  },
  {
    "Country": "Albania",
    "Data_Year": 2016,
    "Happiness_Rank": 109,
    "Happiness_Score": 4.66,
    "Life_Expectancy": 78.1,
    "Population": 2890000,
    "Latitude": 41.153332,
    "Longitude": 20.168331
  },
  {
    "Country": "Albania",
    "Data_Year": 2018,
    "Happiness_Rank": 112,
    "Happiness_Score": 4.59,
    "Life_Expectancy": 78.3,
    "Population": 2880000,
    "Latitude": 41.153332,
    "Longitude": 20.168331
  },
  {
    "Country": "Japan",
    "Data_Year": 2019,
    "Happiness_Rank": 54,
    "Happiness_Score": 5.92,
    "Life_Expectancy": 84.5,
    "Population": 127000000,
    "Latitude": 36.204824,
    "Longitude": 138.252924
  },
  {
    "Country": "Algeria",
    "Data_Year": 2015,
    "Happiness_Rank": 68,
    "Happiness_Score": 5.6,
    "Life_Expectancy": 77.1,
    "Population": 39700000,
    "Latitude": 28.033886,
    "Longitude": 1.659626
  },
  {
    "Country": "Algeria",
    "Data_Year": 2018,
    "Happiness_Rank": 84,
    "Happiness_Score": 5.3,
    "Life_Expectancy": 77.9,
    "Population": 42200000,
    "Latitude": 28.033886,
    "Longitude": 1.659626
  },
  {
    "Country": "Algeria",
    "Data_Year": 2016,
    "Happiness_Rank": 38,
    "Happiness_Score": 6.36,
    "Life_Expectancy": 77.4,
    "Population": 40600000,
    "Latitude": 28.033886,
    "Longitude": 1.659626
  },
  {
    "Country": "Algeria",
    "Data_Year": 2017,
    "Happiness_Rank": 53,
    "Happiness_Score": 5.87,
    "Life_Expectancy": 77.7,
    "Population": 41400000,
    "Latitude": 28.033886,
    "Longitude": 1.659626
  },
  {
    "Country": "Angola",
    "Data_Year": 2015,
    "Happiness_Rank": 137,
    "Happiness_Score": 4.03,
    "Life_Expectancy": 63.3,
    "Population": 27900000,
    "Latitude": -11.202692,
    "Longitude": 17.873887
  },
  {
    "Country": "Angola",
    "Data_Year": 2018,
    "Happiness_Rank": 142,
    "Happiness_Score": 3.8,
    "Life_Expectancy": 64.6,
    "Population": 30800000,
    "Latitude": -11.202692,
    "Longitude": 17.873887
  },
  {
    "Country": "Angola",
    "Data_Year": 2017,
    "Happiness_Rank": 140,
    "Happiness_Score": 3.8,
    "Life_Expectancy": 64.2,
    "Population": 29800000,
    "Latitude": -11.202692,
    "Longitude": 17.873887
  },
  {
    "Country": "Angola",
    "Data_Year": 2016,
    "Happiness_Rank": 141,
    "Happiness_Score": 3.87,
    "Life_Expectancy": 63.8,
    "Population": 28800000,
    "Latitude": -11.202692,
    "Longitude": 17.873887
  },
  {
    "Country": "Switzerland",
    "Data_Year": 2019,
    "Happiness_Rank": 5,
    "Happiness_Score": 7.49,
    "Life_Expectancy": 84.3,
    "Population": 8590000,
    "Latitude": 46.818188,
    "Longitude": 8.227512
  },
  {
    "Country": "Argentina",
    "Data_Year": 2017,
    "Happiness_Rank": 24,
    "Happiness_Score": 6.6,
    "Life_Expectancy": 76.7,
    "Population": 43900000,
    "Latitude": -38.416097,
    "Longitude": -63.616672
  },
  {
    "Country": "Argentina",
    "Data_Year": 2018,
    "Happiness_Rank": 29,
    "Happiness_Score": 6.39,
    "Life_Expectancy": 76.8,
    "Population": 44400000,
    "Latitude": -38.416097,
    "Longitude": -63.616672
  },
  {
    "Country": "Italy",
    "Data_Year": 2019,
    "Happiness_Rank": 47,
    "Happiness_Score": 6,
    "Life_Expectancy": 83.5,
    "Population": 60600000,
    "Latitude": 41.87194,
    "Longitude": 12.56738
  },
  {
    "Country": "Argentina",
    "Data_Year": 2015,
    "Happiness_Rank": 30,
    "Happiness_Score": 6.57,
    "Life_Expectancy": 76.5,
    "Population": 43100000,
    "Latitude": -38.416097,
    "Longitude": -63.616672
  },
  {
    "Country": "Argentina",
    "Data_Year": 2016,
    "Happiness_Rank": 26,
    "Happiness_Score": 6.65,
    "Life_Expectancy": 76.5,
    "Population": 43500000,
    "Latitude": -38.416097,
    "Longitude": -63.616672
  },
  {
    "Country": "Armenia",
    "Data_Year": 2015,
    "Happiness_Rank": 127,
    "Happiness_Score": 4.35,
    "Life_Expectancy": 75.3,
    "Population": 2930000,
    "Latitude": 40.069099,
    "Longitude": 45.038189
  },
  {
    "Country": "Armenia",
    "Data_Year": 2018,
    "Happiness_Rank": 129,
    "Happiness_Score": 4.32,
    "Life_Expectancy": 75.8,
    "Population": 2950000,
    "Latitude": 40.069099,
    "Longitude": 45.038189
  },
  {
    "Country": "Armenia",
    "Data_Year": 2017,
    "Happiness_Rank": 121,
    "Happiness_Score": 4.38,
    "Life_Expectancy": 75.6,
    "Population": 2940000,
    "Latitude": 40.069099,
    "Longitude": 45.038189
  },
  {
    "Country": "Armenia",
    "Data_Year": 2016,
    "Happiness_Rank": 121,
    "Happiness_Score": 4.36,
    "Life_Expectancy": 75.4,
    "Population": 2940000,
    "Latitude": 40.069099,
    "Longitude": 45.038189
  },
  {
    "Country": "Israel",
    "Data_Year": 2019,
    "Happiness_Rank": 19,
    "Happiness_Score": 6.81,
    "Life_Expectancy": 83.3,
    "Population": 8520000,
    "Latitude": 31.046051,
    "Longitude": 34.851612
  },
  {
    "Country": "Australia",
    "Data_Year": 2017,
    "Happiness_Rank": 10,
    "Happiness_Score": 7.28,
    "Life_Expectancy": 82.4,
    "Population": 24600000,
    "Latitude": -25.274398,
    "Longitude": 133.775136
  },
  {
    "Country": "Australia",
    "Data_Year": 2016,
    "Happiness_Rank": 9,
    "Happiness_Score": 7.31,
    "Life_Expectancy": 82.5,
    "Population": 24300000,
    "Latitude": -25.274398,
    "Longitude": 133.775136
  },
  {
    "Country": "Australia",
    "Data_Year": 2015,
    "Happiness_Rank": 10,
    "Happiness_Score": 7.28,
    "Life_Expectancy": 82.5,
    "Population": 23900000,
    "Latitude": -25.274398,
    "Longitude": 133.775136
  },
  {
    "Country": "Spain",
    "Data_Year": 2019,
    "Happiness_Rank": 36,
    "Happiness_Score": 6.31,
    "Life_Expectancy": 83.3,
    "Population": 46700000,
    "Latitude": 40.463667,
    "Longitude": -3.74922
  },
  {
    "Country": "Australia",
    "Data_Year": 2018,
    "Happiness_Rank": 10,
    "Happiness_Score": 7.27,
    "Life_Expectancy": 82.5,
    "Population": 24900000,
    "Latitude": -25.274398,
    "Longitude": 133.775136
  },
  {
    "Country": "Kuwait",
    "Data_Year": 2019,
    "Happiness_Rank": 45,
    "Happiness_Score": 6.08,
    "Life_Expectancy": 83.3,
    "Population": 4210000,
    "Latitude": 29.31166,
    "Longitude": 47.481766
  },
  {
    "Country": "Austria",
    "Data_Year": 2016,
    "Happiness_Rank": 12,
    "Happiness_Score": 7.12,
    "Life_Expectancy": 81.7,
    "Population": 8750000,
    "Latitude": 47.516231,
    "Longitude": 14.550072
  },
  {
    "Country": "Austria",
    "Data_Year": 2015,
    "Happiness_Rank": 13,
    "Happiness_Score": 7.2,
    "Life_Expectancy": 81.5,
    "Population": 8680000,
    "Latitude": 47.516231,
    "Longitude": 14.550072
  },
  {
    "Country": "Austria",
    "Data_Year": 2018,
    "Happiness_Rank": 12,
    "Happiness_Score": 7.14,
    "Life_Expectancy": 81.9,
    "Population": 8890000,
    "Latitude": 47.516231,
    "Longitude": 14.550072
  },
  {
    "Country": "Austria",
    "Data_Year": 2017,
    "Happiness_Rank": 13,
    "Happiness_Score": 7.01,
    "Life_Expectancy": 81.8,
    "Population": 8820000,
    "Latitude": 47.516231,
    "Longitude": 14.550072
  },
  {
    "Country": "Azerbaijan",
    "Data_Year": 2018,
    "Happiness_Rank": 87,
    "Happiness_Score": 5.2,
    "Life_Expectancy": 70.9,
    "Population": 9950000,
    "Latitude": 40.143105,
    "Longitude": 47.576927
  },
  {
    "Country": "Azerbaijan",
    "Data_Year": 2017,
    "Happiness_Rank": 85,
    "Happiness_Score": 5.23,
    "Life_Expectancy": 70.8,
    "Population": 9850000,
    "Latitude": 40.143105,
    "Longitude": 47.576927
  },
  {
    "Country": "France",
    "Data_Year": 2019,
    "Happiness_Rank": 23,
    "Happiness_Score": 6.49,
    "Life_Expectancy": 83.1,
    "Population": 65100000,
    "Latitude": 46.227638,
    "Longitude": 2.213749
  },
  {
    "Country": "Azerbaijan",
    "Data_Year": 2015,
    "Happiness_Rank": 80,
    "Happiness_Score": 5.21,
    "Life_Expectancy": 70.5,
    "Population": 9620000,
    "Latitude": 40.143105,
    "Longitude": 47.576927
  },
  {
    "Country": "Azerbaijan",
    "Data_Year": 2016,
    "Happiness_Rank": 81,
    "Happiness_Score": 5.29,
    "Life_Expectancy": 70.6,
    "Population": 9740000,
    "Latitude": 40.143105,
    "Longitude": 47.576927
  },
  {
    "Country": "Iceland",
    "Data_Year": 2019,
    "Happiness_Rank": 4,
    "Happiness_Score": 7.5,
    "Life_Expectancy": 83,
    "Population": 339000,
    "Latitude": 64.963051,
    "Longitude": -19.020835
  },
  {
    "Country": "Bahrain",
    "Data_Year": 2017,
    "Happiness_Rank": 41,
    "Happiness_Score": 6.09,
    "Life_Expectancy": 79.5,
    "Population": 1490000,
    "Latitude": 25.930414,
    "Longitude": 50.637772
  },
  {
    "Country": "Bahrain",
    "Data_Year": 2015,
    "Happiness_Rank": 49,
    "Happiness_Score": 5.96,
    "Life_Expectancy": 79.3,
    "Population": 1370000,
    "Latitude": 25.930414,
    "Longitude": 50.637772
  },
  {
    "Country": "Bahrain",
    "Data_Year": 2016,
    "Happiness_Rank": 42,
    "Happiness_Score": 6.22,
    "Life_Expectancy": 79.4,
    "Population": 1430000,
    "Latitude": 25.930414,
    "Longitude": 50.637772
  },
  {
    "Country": "Bahrain",
    "Data_Year": 2018,
    "Happiness_Rank": 43,
    "Happiness_Score": 6.1,
    "Life_Expectancy": 79.6,
    "Population": 1570000,
    "Latitude": 25.930414,
    "Longitude": 50.637772
  },
  {
    "Country": "Bangladesh",
    "Data_Year": 2017,
    "Happiness_Rank": 110,
    "Happiness_Score": 4.61,
    "Life_Expectancy": 73.1,
    "Population": 160000000,
    "Latitude": 23.684994,
    "Longitude": 90.356331
  },
  {
    "Country": "Bangladesh",
    "Data_Year": 2016,
    "Happiness_Rank": 110,
    "Happiness_Score": 4.64,
    "Life_Expectancy": 72.9,
    "Population": 158000000,
    "Latitude": 23.684994,
    "Longitude": 90.356331
  },
  {
    "Country": "Bangladesh",
    "Data_Year": 2018,
    "Happiness_Rank": 115,
    "Happiness_Score": 4.5,
    "Life_Expectancy": 73.4,
    "Population": 161000000,
    "Latitude": 23.684994,
    "Longitude": 90.356331
  },
  {
    "Country": "South Korea",
    "Data_Year": 2019,
    "Happiness_Rank": 57,
    "Happiness_Score": 5.88,
    "Life_Expectancy": 83,
    "Population": 51200000,
    "Latitude": 35.9078,
    "Longitude": 127.7669
  },
  {
    "Country": "Bangladesh",
    "Data_Year": 2015,
    "Happiness_Rank": 109,
    "Happiness_Score": 4.69,
    "Life_Expectancy": 72.5,
    "Population": 156000000,
    "Latitude": 23.684994,
    "Longitude": 90.356331
  },
  {
    "Country": "Belarus",
    "Data_Year": 2017,
    "Happiness_Rank": 67,
    "Happiness_Score": 5.57,
    "Life_Expectancy": 74,
    "Population": 9450000,
    "Latitude": 53.709807,
    "Longitude": 27.953389
  },
  {
    "Country": "Belarus",
    "Data_Year": 2015,
    "Happiness_Rank": 59,
    "Happiness_Score": 5.81,
    "Life_Expectancy": 73.8,
    "Population": 9440000,
    "Latitude": 53.709807,
    "Longitude": 27.953389
  },
  {
    "Country": "Belarus",
    "Data_Year": 2018,
    "Happiness_Rank": 73,
    "Happiness_Score": 5.48,
    "Life_Expectancy": 74.3,
    "Population": 9450000,
    "Latitude": 53.709807,
    "Longitude": 27.953389
  },
  {
    "Country": "Sweden",
    "Data_Year": 2019,
    "Happiness_Rank": 9,
    "Happiness_Score": 7.31,
    "Life_Expectancy": 82.8,
    "Population": 10000000,
    "Latitude": 60.128161,
    "Longitude": 18.643501
  },
  {
    "Country": "Belarus",
    "Data_Year": 2016,
    "Happiness_Rank": 61,
    "Happiness_Score": 5.8,
    "Life_Expectancy": 74,
    "Population": 9450000,
    "Latitude": 53.709807,
    "Longitude": 27.953389
  },
  {
    "Country": "Belgium",
    "Data_Year": 2015,
    "Happiness_Rank": 19,
    "Happiness_Score": 6.94,
    "Life_Expectancy": 80.9,
    "Population": 11300000,
    "Latitude": 50.503887,
    "Longitude": 4.469936
  },
  {
    "Country": "Belgium",
    "Data_Year": 2017,
    "Happiness_Rank": 17,
    "Happiness_Score": 6.89,
    "Life_Expectancy": 81.4,
    "Population": 11400000,
    "Latitude": 50.503887,
    "Longitude": 4.469936
  },
  {
    "Country": "Belgium",
    "Data_Year": 2018,
    "Happiness_Rank": 16,
    "Happiness_Score": 6.93,
    "Life_Expectancy": 81.5,
    "Population": 11500000,
    "Latitude": 50.503887,
    "Longitude": 4.469936
  },
  {
    "Country": "Belgium",
    "Data_Year": 2016,
    "Happiness_Rank": 18,
    "Happiness_Score": 6.93,
    "Life_Expectancy": 81.2,
    "Population": 11400000,
    "Latitude": 50.503887,
    "Longitude": 4.469936
  },
  {
    "Country": "Australia",
    "Data_Year": 2019,
    "Happiness_Rank": 10,
    "Happiness_Score": 7.27,
    "Life_Expectancy": 82.7,
    "Population": 25200000,
    "Latitude": -25.274398,
    "Longitude": 133.775136
  },
  {
    "Country": "Belize",
    "Data_Year": 2017,
    "Happiness_Rank": 50,
    "Happiness_Score": 5.96,
    "Life_Expectancy": 74.2,
    "Population": 376000,
    "Latitude": 17.189877,
    "Longitude": -88.49765
  },
  {
    "Country": "Norway",
    "Data_Year": 2019,
    "Happiness_Rank": 2,
    "Happiness_Score": 7.59,
    "Life_Expectancy": 82.6,
    "Population": 5380000,
    "Latitude": 60.472024,
    "Longitude": 8.468946
  },
  {
    "Country": "Belize",
    "Data_Year": 2018,
    "Happiness_Rank": 49,
    "Happiness_Score": 5.96,
    "Life_Expectancy": 74.3,
    "Population": 383000,
    "Latitude": 17.189877,
    "Longitude": -88.49765
  },
  {
    "Country": "Belize",
    "Data_Year": 2016,
    "Happiness_Rank": 52,
    "Happiness_Score": 5.96,
    "Life_Expectancy": 74.1,
    "Population": 368000,
    "Latitude": 17.189877,
    "Longitude": -88.49765
  },
  {
    "Country": "Benin",
    "Data_Year": 2017,
    "Happiness_Rank": 143,
    "Happiness_Score": 3.66,
    "Life_Expectancy": 64.6,
    "Population": 11200000,
    "Latitude": 9.30769,
    "Longitude": 2.315834
  },
  {
    "Country": "Ireland",
    "Data_Year": 2019,
    "Happiness_Rank": 14,
    "Happiness_Score": 6.98,
    "Life_Expectancy": 82.3,
    "Population": 4880000,
    "Latitude": 53.41291,
    "Longitude": -8.24389
  },
  {
    "Country": "Benin",
    "Data_Year": 2018,
    "Happiness_Rank": 136,
    "Happiness_Score": 4.14,
    "Life_Expectancy": 64.9,
    "Population": 11500000,
    "Latitude": 9.30769,
    "Longitude": 2.315834
  },
  {
    "Country": "Benin",
    "Data_Year": 2016,
    "Happiness_Rank": 153,
    "Happiness_Score": 3.48,
    "Life_Expectancy": 64.1,
    "Population": 10900000,
    "Latitude": 9.30769,
    "Longitude": 2.315834
  },
  {
    "Country": "Benin",
    "Data_Year": 2015,
    "Happiness_Rank": 155,
    "Happiness_Score": 3.34,
    "Life_Expectancy": 63.5,
    "Population": 10600000,
    "Latitude": 9.30769,
    "Longitude": 2.315834
  },
  {
    "Country": "Bhutan",
    "Data_Year": 2018,
    "Happiness_Rank": 97,
    "Happiness_Score": 5.08,
    "Life_Expectancy": 74.4,
    "Population": 754000,
    "Latitude": 27.514162,
    "Longitude": 90.433601
  },
  {
    "Country": "Bhutan",
    "Data_Year": 2015,
    "Happiness_Rank": 79,
    "Happiness_Score": 5.25,
    "Life_Expectancy": 73.5,
    "Population": 728000,
    "Latitude": 27.514162,
    "Longitude": 90.433601
  },
  {
    "Country": "Bhutan",
    "Data_Year": 2017,
    "Happiness_Rank": 97,
    "Happiness_Score": 5.01,
    "Life_Expectancy": 74,
    "Population": 746000,
    "Latitude": 27.514162,
    "Longitude": 90.433601
  },
  {
    "Country": "Bhutan",
    "Data_Year": 2016,
    "Happiness_Rank": 84,
    "Happiness_Score": 5.2,
    "Life_Expectancy": 73.8,
    "Population": 737000,
    "Latitude": 27.514162,
    "Longitude": 90.433601
  },
  {
    "Country": "Canada",
    "Data_Year": 2019,
    "Happiness_Rank": 7,
    "Happiness_Score": 7.33,
    "Life_Expectancy": 82.2,
    "Population": 37400000,
    "Latitude": 56.130366,
    "Longitude": -106.346771
  },
  {
    "Country": "Bolivia",
    "Data_Year": 2017,
    "Happiness_Rank": 58,
    "Happiness_Score": 5.82,
    "Life_Expectancy": 72.8,
    "Population": 11200000,
    "Latitude": -16.290154,
    "Longitude": -63.588653
  },
  {
    "Country": "Bolivia",
    "Data_Year": 2015,
    "Happiness_Rank": 51,
    "Happiness_Score": 5.89,
    "Life_Expectancy": 72.2,
    "Population": 10900000,
    "Latitude": -16.290154,
    "Longitude": -63.588653
  },
  {
    "Country": "Austria",
    "Data_Year": 2019,
    "Happiness_Rank": 12,
    "Happiness_Score": 7.14,
    "Life_Expectancy": 82,
    "Population": 8960000,
    "Latitude": 47.516231,
    "Longitude": 14.550072
  },
  {
    "Country": "Bolivia",
    "Data_Year": 2018,
    "Happiness_Rank": 62,
    "Happiness_Score": 5.75,
    "Life_Expectancy": 73.1,
    "Population": 11400000,
    "Latitude": -16.290154,
    "Longitude": -63.588653
  },
  {
    "Country": "Bolivia",
    "Data_Year": 2016,
    "Happiness_Rank": 59,
    "Happiness_Score": 5.82,
    "Life_Expectancy": 72.5,
    "Population": 11000000,
    "Latitude": -16.290154,
    "Longitude": -63.588653
  },
  {
    "Country": "Bosnia and Herzegovina",
    "Data_Year": 2017,
    "Happiness_Rank": 90,
    "Happiness_Score": 5.18,
    "Life_Expectancy": 76.7,
    "Population": 3350000,
    "Latitude": 43.9143,
    "Longitude": 17.6791
  },
  {
    "Country": "Bosnia and Herzegovina",
    "Data_Year": 2018,
    "Happiness_Rank": 93,
    "Happiness_Score": 5.13,
    "Life_Expectancy": 76.9,
    "Population": 3320000,
    "Latitude": 43.9143,
    "Longitude": 17.6791
  },
  {
    "Country": "Luxembourg",
    "Data_Year": 2019,
    "Happiness_Rank": 17,
    "Happiness_Score": 6.91,
    "Life_Expectancy": 82,
    "Population": 616000,
    "Latitude": 49.815273,
    "Longitude": 6.129583
  },
  {
    "Country": "Bosnia and Herzegovina",
    "Data_Year": 2016,
    "Happiness_Rank": 87,
    "Happiness_Score": 5.16,
    "Life_Expectancy": 76.5,
    "Population": 3390000,
    "Latitude": 43.9143,
    "Longitude": 17.6791
  },
  {
    "Country": "Bosnia and Herzegovina",
    "Data_Year": 2015,
    "Happiness_Rank": 96,
    "Happiness_Score": 4.95,
    "Life_Expectancy": 76.4,
    "Population": 3430000,
    "Latitude": 43.9143,
    "Longitude": 17.6791
  },
  {
    "Country": "Botswana",
    "Data_Year": 2015,
    "Happiness_Rank": 128,
    "Happiness_Score": 4.33,
    "Life_Expectancy": 66.9,
    "Population": 2120000,
    "Latitude": -22.328474,
    "Longitude": 24.684866
  },
  {
    "Country": "Botswana",
    "Data_Year": 2018,
    "Happiness_Rank": 146,
    "Happiness_Score": 3.59,
    "Life_Expectancy": 69.5,
    "Population": 2250000,
    "Latitude": -22.328474,
    "Longitude": 24.684866
  },
  {
    "Country": "Cyprus",
    "Data_Year": 2019,
    "Happiness_Rank": 61,
    "Happiness_Score": 5.76,
    "Life_Expectancy": 82,
    "Population": 1200000,
    "Latitude": 35.126413,
    "Longitude": 33.429859
  },
  {
    "Country": "Botswana",
    "Data_Year": 2017,
    "Happiness_Rank": 142,
    "Happiness_Score": 3.77,
    "Life_Expectancy": 69.1,
    "Population": 2210000,
    "Latitude": -22.328474,
    "Longitude": 24.684866
  },
  {
    "Country": "Botswana",
    "Data_Year": 2016,
    "Happiness_Rank": 137,
    "Happiness_Score": 3.97,
    "Life_Expectancy": 68.1,
    "Population": 2160000,
    "Latitude": -22.328474,
    "Longitude": 24.684866
  },
  {
    "Country": "Brazil",
    "Data_Year": 2015,
    "Happiness_Rank": 16,
    "Happiness_Score": 6.98,
    "Life_Expectancy": 75.5,
    "Population": 204000000,
    "Latitude": -14.235004,
    "Longitude": -51.92528
  },
  {
    "Country": "Brazil",
    "Data_Year": 2017,
    "Happiness_Rank": 22,
    "Happiness_Score": 6.64,
    "Life_Expectancy": 75.5,
    "Population": 208000000,
    "Latitude": -14.235004,
    "Longitude": -51.92528
  },
  {
    "Country": "New Zealand",
    "Data_Year": 2019,
    "Happiness_Rank": 8,
    "Happiness_Score": 7.32,
    "Life_Expectancy": 81.9,
    "Population": 4780000,
    "Latitude": 40.9006,
    "Longitude": -174.886
  },
  {
    "Country": "Brazil",
    "Data_Year": 2016,
    "Happiness_Rank": 17,
    "Happiness_Score": 6.95,
    "Life_Expectancy": 75.4,
    "Population": 206000000,
    "Latitude": -14.235004,
    "Longitude": -51.92528
  },
  {
    "Country": "Brazil",
    "Data_Year": 2018,
    "Happiness_Rank": 28,
    "Happiness_Score": 6.42,
    "Life_Expectancy": 75.7,
    "Population": 209000000,
    "Latitude": -14.235004,
    "Longitude": -51.92528
  },
  {
    "Country": "Bulgaria",
    "Data_Year": 2017,
    "Happiness_Rank": 105,
    "Happiness_Score": 4.71,
    "Life_Expectancy": 74.9,
    "Population": 7100000,
    "Latitude": 42.733883,
    "Longitude": 25.48583
  },
  {
    "Country": "Bulgaria",
    "Data_Year": 2015,
    "Happiness_Rank": 134,
    "Happiness_Score": 4.22,
    "Life_Expectancy": 74.8,
    "Population": 7200000,
    "Latitude": 42.733883,
    "Longitude": 25.48583
  },
  {
    "Country": "Bulgaria",
    "Data_Year": 2016,
    "Happiness_Rank": 129,
    "Happiness_Score": 4.22,
    "Life_Expectancy": 74.9,
    "Population": 7150000,
    "Latitude": 42.733883,
    "Longitude": 25.48583
  },
  {
    "Country": "Finland",
    "Data_Year": 2019,
    "Happiness_Rank": 1,
    "Happiness_Score": 7.63,
    "Life_Expectancy": 81.8,
    "Population": 5530000,
    "Latitude": 61.92411,
    "Longitude": 25.748151
  },
  {
    "Country": "Bulgaria",
    "Data_Year": 2018,
    "Happiness_Rank": 100,
    "Happiness_Score": 4.93,
    "Life_Expectancy": 75,
    "Population": 7050000,
    "Latitude": 42.733883,
    "Longitude": 25.48583
  },
  {
    "Country": "Netherlands",
    "Data_Year": 2019,
    "Happiness_Rank": 6,
    "Happiness_Score": 7.44,
    "Life_Expectancy": 81.8,
    "Population": 17100000,
    "Latitude": 52.132633,
    "Longitude": 5.291266
  },
  {
    "Country": "Burkina Faso",
    "Data_Year": 2015,
    "Happiness_Rank": 152,
    "Happiness_Score": 3.59,
    "Life_Expectancy": 60.7,
    "Population": 18100000,
    "Latitude": 12.2383,
    "Longitude": 1.5616
  },
  {
    "Country": "Burkina Faso",
    "Data_Year": 2016,
    "Happiness_Rank": 145,
    "Happiness_Score": 3.74,
    "Life_Expectancy": 61.2,
    "Population": 18600000,
    "Latitude": 12.2383,
    "Longitude": 1.5616
  },
  {
    "Country": "Burkina Faso",
    "Data_Year": 2018,
    "Happiness_Rank": 121,
    "Happiness_Score": 4.42,
    "Life_Expectancy": 62.1,
    "Population": 19800000,
    "Latitude": 12.2383,
    "Longitude": 1.5616
  },
  {
    "Country": "Burkina Faso",
    "Data_Year": 2017,
    "Happiness_Rank": 134,
    "Happiness_Score": 4.03,
    "Life_Expectancy": 61.7,
    "Population": 19200000,
    "Latitude": 12.2383,
    "Longitude": 1.5616
  },
  {
    "Country": "Burundi",
    "Data_Year": 2015,
    "Happiness_Rank": 157,
    "Happiness_Score": 2.9,
    "Life_Expectancy": 60.8,
    "Population": 10200000,
    "Latitude": -3.373056,
    "Longitude": 29.918886
  },
  {
    "Country": "Burundi",
    "Data_Year": 2016,
    "Happiness_Rank": 157,
    "Happiness_Score": 2.9,
    "Life_Expectancy": 61.2,
    "Population": 10500000,
    "Latitude": -3.373056,
    "Longitude": 29.918886
  },
  {
    "Country": "Burundi",
    "Data_Year": 2017,
    "Happiness_Rank": 154,
    "Happiness_Score": 2.9,
    "Life_Expectancy": 61.5,
    "Population": 10800000,
    "Latitude": -3.373056,
    "Longitude": 29.918886
  },
  {
    "Country": "Portugal",
    "Data_Year": 2019,
    "Happiness_Rank": 77,
    "Happiness_Score": 5.41,
    "Life_Expectancy": 81.8,
    "Population": 10200000,
    "Latitude": 39.399872,
    "Longitude": -8.224454
  },
  {
    "Country": "Burundi",
    "Data_Year": 2018,
    "Happiness_Rank": 156,
    "Happiness_Score": 2.9,
    "Life_Expectancy": 61.9,
    "Population": 11200000,
    "Latitude": -3.373056,
    "Longitude": 29.918886
  },
  {
    "Country": "Cambodia",
    "Data_Year": 2017,
    "Happiness_Rank": 129,
    "Happiness_Score": 4.17,
    "Life_Expectancy": 69.9,
    "Population": 16000000,
    "Latitude": 12.565679,
    "Longitude": 104.990963
  },
  {
    "Country": "Cambodia",
    "Data_Year": 2018,
    "Happiness_Rank": 120,
    "Happiness_Score": 4.43,
    "Life_Expectancy": 70.2,
    "Population": 16200000,
    "Latitude": 12.565679,
    "Longitude": 104.990963
  },
  {
    "Country": "Belgium",
    "Data_Year": 2019,
    "Happiness_Rank": 16,
    "Happiness_Score": 6.93,
    "Life_Expectancy": 81.7,
    "Population": 11500000,
    "Latitude": 50.503887,
    "Longitude": 4.469936
  },
  {
    "Country": "Cambodia",
    "Data_Year": 2016,
    "Happiness_Rank": 140,
    "Happiness_Score": 3.91,
    "Life_Expectancy": 69.6,
    "Population": 15800000,
    "Latitude": 12.565679,
    "Longitude": 104.990963
  },
  {
    "Country": "Cambodia",
    "Data_Year": 2015,
    "Happiness_Rank": 145,
    "Happiness_Score": 3.82,
    "Life_Expectancy": 69.3,
    "Population": 15500000,
    "Latitude": 12.565679,
    "Longitude": 104.990963
  },
  {
    "Country": "Slovenia",
    "Data_Year": 2019,
    "Happiness_Rank": 51,
    "Happiness_Score": 5.95,
    "Life_Expectancy": 81.4,
    "Population": 2080000,
    "Latitude": 46.151241,
    "Longitude": 14.995463
  },
  {
    "Country": "Cameroon",
    "Data_Year": 2015,
    "Happiness_Rank": 133,
    "Happiness_Score": 4.25,
    "Life_Expectancy": 61.2,
    "Population": 23300000,
    "Latitude": 7.369722,
    "Longitude": 12.354722
  },
  {
    "Country": "Cameroon",
    "Data_Year": 2018,
    "Happiness_Rank": 99,
    "Happiness_Score": 4.97,
    "Life_Expectancy": 63.4,
    "Population": 25200000,
    "Latitude": 7.369722,
    "Longitude": 12.354722
  },
  {
    "Country": "Cameroon",
    "Data_Year": 2016,
    "Happiness_Rank": 114,
    "Happiness_Score": 4.51,
    "Life_Expectancy": 62.1,
    "Population": 23900000,
    "Latitude": 7.369722,
    "Longitude": 12.354722
  },
  {
    "Country": "Cameroon",
    "Data_Year": 2017,
    "Happiness_Rank": 107,
    "Happiness_Score": 4.7,
    "Life_Expectancy": 63,
    "Population": 24600000,
    "Latitude": 7.369722,
    "Longitude": 12.354722
  },
  {
    "Country": "Canada",
    "Data_Year": 2018,
    "Happiness_Rank": 7,
    "Happiness_Score": 7.33,
    "Life_Expectancy": 82.1,
    "Population": 37100000,
    "Latitude": 56.130366,
    "Longitude": -106.346771
  },
  {
    "Country": "Malta",
    "Data_Year": 2019,
    "Happiness_Rank": 22,
    "Happiness_Score": 6.63,
    "Life_Expectancy": 81.3,
    "Population": 440000,
    "Latitude": 35.937496,
    "Longitude": 14.375416
  },
  {
    "Country": "Canada",
    "Data_Year": 2015,
    "Happiness_Rank": 5,
    "Happiness_Score": 7.43,
    "Life_Expectancy": 81.7,
    "Population": 36000000,
    "Latitude": 56.130366,
    "Longitude": -106.346771
  },
  {
    "Country": "Canada",
    "Data_Year": 2016,
    "Happiness_Rank": 6,
    "Happiness_Score": 7.4,
    "Life_Expectancy": 81.9,
    "Population": 36400000,
    "Latitude": 56.130366,
    "Longitude": -106.346771
  },
  {
    "Country": "Canada",
    "Data_Year": 2017,
    "Happiness_Rank": 7,
    "Happiness_Score": 7.32,
    "Life_Expectancy": 82,
    "Population": 36700000,
    "Latitude": 56.130366,
    "Longitude": -106.346771
  },
  {
    "Country": "Central African Republic",
    "Data_Year": 2017,
    "Happiness_Rank": 155,
    "Happiness_Score": 2.69,
    "Life_Expectancy": 51.9,
    "Population": 4600000,
    "Latitude": 6.6111,
    "Longitude": 20.9394
  },
  {
    "Country": "Greece",
    "Data_Year": 2019,
    "Happiness_Rank": 79,
    "Happiness_Score": 5.36,
    "Life_Expectancy": 81.3,
    "Population": 10500000,
    "Latitude": 39.074208,
    "Longitude": 21.824312
  },
  {
    "Country": "Central African Republic",
    "Data_Year": 2015,
    "Happiness_Rank": 148,
    "Happiness_Score": 3.68,
    "Life_Expectancy": 50.9,
    "Population": 4490000,
    "Latitude": 6.6111,
    "Longitude": 20.9394
  },
  {
    "Country": "Central African Republic",
    "Data_Year": 2018,
    "Happiness_Rank": 155,
    "Happiness_Score": 3.08,
    "Life_Expectancy": 52.4,
    "Population": 4670000,
    "Latitude": 6.6111,
    "Longitude": 20.9394
  },
  {
    "Country": "Chad",
    "Data_Year": 2017,
    "Happiness_Rank": 137,
    "Happiness_Score": 3.94,
    "Life_Expectancy": 60,
    "Population": 15000000,
    "Latitude": 15.454166,
    "Longitude": 18.732207
  },
  {
    "Country": "Chad",
    "Data_Year": 2015,
    "Happiness_Rank": 149,
    "Happiness_Score": 3.67,
    "Life_Expectancy": 59.2,
    "Population": 14100000,
    "Latitude": 15.454166,
    "Longitude": 18.732207
  },
  {
    "Country": "Chad",
    "Data_Year": 2016,
    "Happiness_Rank": 144,
    "Happiness_Score": 3.76,
    "Life_Expectancy": 59.7,
    "Population": 14600000,
    "Latitude": 15.454166,
    "Longitude": 18.732207
  },
  {
    "Country": "Chad",
    "Data_Year": 2018,
    "Happiness_Rank": 131,
    "Happiness_Score": 4.3,
    "Life_Expectancy": 60.3,
    "Population": 15500000,
    "Latitude": 15.454166,
    "Longitude": 18.732207
  },
  {
    "Country": "United Kingdom",
    "Data_Year": 2019,
    "Happiness_Rank": 11,
    "Happiness_Score": 7.19,
    "Life_Expectancy": 81.1,
    "Population": 67500000,
    "Latitude": 55.3781,
    "Longitude": 3.436
  },
  {
    "Country": "Chile",
    "Data_Year": 2015,
    "Happiness_Rank": 27,
    "Happiness_Score": 6.67,
    "Life_Expectancy": 79.6,
    "Population": 18000000,
    "Latitude": -35.675147,
    "Longitude": -71.542969
  },
  {
    "Country": "Chile",
    "Data_Year": 2018,
    "Happiness_Rank": 25,
    "Happiness_Score": 6.48,
    "Life_Expectancy": 79.8,
    "Population": 18700000,
    "Latitude": -35.675147,
    "Longitude": -71.542969
  },
  {
    "Country": "Chile",
    "Data_Year": 2016,
    "Happiness_Rank": 24,
    "Happiness_Score": 6.7,
    "Life_Expectancy": 79.7,
    "Population": 18200000,
    "Latitude": -35.675147,
    "Longitude": -71.542969
  },
  {
    "Country": "Denmark",
    "Data_Year": 2019,
    "Happiness_Rank": 3,
    "Happiness_Score": 7.56,
    "Life_Expectancy": 81,
    "Population": 5770000,
    "Latitude": 56.26392,
    "Longitude": 9.501785
  },
  {
    "Country": "Chile",
    "Data_Year": 2017,
    "Happiness_Rank": 20,
    "Happiness_Score": 6.65,
    "Life_Expectancy": 79.7,
    "Population": 18500000,
    "Latitude": -35.675147,
    "Longitude": -71.542969
  },
  {
    "Country": "China",
    "Data_Year": 2017,
    "Happiness_Rank": 79,
    "Happiness_Score": 5.27,
    "Life_Expectancy": 77.1,
    "Population": 1420000000,
    "Latitude": 35.86166,
    "Longitude": 104.195397
  },
  {
    "Country": "China",
    "Data_Year": 2018,
    "Happiness_Rank": 86,
    "Happiness_Score": 5.25,
    "Life_Expectancy": 77.3,
    "Population": 1430000000,
    "Latitude": 35.86166,
    "Longitude": 104.195397
  },
  {
    "Country": "Germany",
    "Data_Year": 2019,
    "Happiness_Rank": 15,
    "Happiness_Score": 6.96,
    "Life_Expectancy": 80.9,
    "Population": 83500000,
    "Latitude": 51.165691,
    "Longitude": 10.451526
  },
  {
    "Country": "China",
    "Data_Year": 2015,
    "Happiness_Rank": 84,
    "Happiness_Score": 5.14,
    "Life_Expectancy": 76.5,
    "Population": 1410000000,
    "Latitude": 35.86166,
    "Longitude": 104.195397
  },
  {
    "Country": "China",
    "Data_Year": 2016,
    "Happiness_Rank": 83,
    "Happiness_Score": 5.24,
    "Life_Expectancy": 76.7,
    "Population": 1410000000,
    "Latitude": 35.86166,
    "Longitude": 104.195397
  },
  {
    "Country": "Colombia",
    "Data_Year": 2016,
    "Happiness_Rank": 31,
    "Happiness_Score": 6.48,
    "Life_Expectancy": 80,
    "Population": 48200000,
    "Latitude": 4.570868,
    "Longitude": -74.297333
  },
  {
    "Country": "Northern Cyprus",
    "Data_Year": 2019,
    "Happiness_Rank": 58,
    "Happiness_Score": 5.84,
    "Life_Expectancy": 80.9,
    "Population": 1198575,
    "Latitude": 35.248,
    "Longitude": 33.6577
  },
  {
    "Country": "Colombia",
    "Data_Year": 2017,
    "Happiness_Rank": 36,
    "Happiness_Score": 6.36,
    "Life_Expectancy": 80.1,
    "Population": 48900000,
    "Latitude": 4.570868,
    "Longitude": -74.297333
  },
  {
    "Country": "Colombia",
    "Data_Year": 2018,
    "Happiness_Rank": 37,
    "Happiness_Score": 6.26,
    "Life_Expectancy": 80.3,
    "Population": 49700000,
    "Latitude": 4.570868,
    "Longitude": -74.297333
  },
  {
    "Country": "Colombia",
    "Data_Year": 2015,
    "Happiness_Rank": 33,
    "Happiness_Score": 6.48,
    "Life_Expectancy": 80,
    "Population": 47500000,
    "Latitude": 4.570868,
    "Longitude": -74.297333
  },
  {
    "Country": "Comoros",
    "Data_Year": 2015,
    "Happiness_Rank": 140,
    "Happiness_Score": 3.96,
    "Life_Expectancy": 68,
    "Population": 777000,
    "Latitude": -11.875001,
    "Longitude": 43.872219
  },
  {
    "Country": "Comoros",
    "Data_Year": 2016,
    "Happiness_Rank": 138,
    "Happiness_Score": 3.96,
    "Life_Expectancy": 68.3,
    "Population": 796000,
    "Latitude": -11.875001,
    "Longitude": 43.872219
  },
  {
    "Country": "Peru",
    "Data_Year": 2019,
    "Happiness_Rank": 65,
    "Happiness_Score": 5.66,
    "Life_Expectancy": 80.8,
    "Population": 32500000,
    "Latitude": -9.189967,
    "Longitude": -75.015152
  },
  {
    "Country": "Congo (Brazzaville)",
    "Data_Year": 2015,
    "Happiness_Rank": 139,
    "Happiness_Score": 3.99,
    "Life_Expectancy": 62.5,
    "Population": 4980000,
    "Latitude": 0.228,
    "Longitude": 15.8277
  },
  {
    "Country": "Congo (Brazzaville)",
    "Data_Year": 2018,
    "Happiness_Rank": 114,
    "Happiness_Score": 4.56,
    "Life_Expectancy": 62.6,
    "Population": 5110000,
    "Latitude": 0.228,
    "Longitude": 15.8277
  },
  {
    "Country": "Congo (Brazzaville)",
    "Data_Year": 2017,
    "Happiness_Rank": 124,
    "Happiness_Score": 4.29,
    "Life_Expectancy": 63,
    "Population": 5240000,
    "Latitude": 0.228,
    "Longitude": 15.8277
  },
  {
    "Country": "Congo (Brazzaville)",
    "Data_Year": 2016,
    "Happiness_Rank": 127,
    "Happiness_Score": 4.24,
    "Life_Expectancy": 63.3,
    "Population": 5380000,
    "Latitude": 0.228,
    "Longitude": 15.8277
  },
  {
    "Country": "Congo (Kinshasa)",
    "Data_Year": 2016,
    "Happiness_Rank": 125,
    "Happiness_Score": 4.27,
    "Life_Expectancy": 61.3,
    "Population": 76200000,
    "Latitude": 4.0383,
    "Longitude": 21.7587
  },
  {
    "Country": "Congo (Kinshasa)",
    "Data_Year": 2018,
    "Happiness_Rank": 132,
    "Happiness_Score": 4.24,
    "Life_Expectancy": 61.9,
    "Population": 78800000,
    "Latitude": 4.0383,
    "Longitude": 21.7587
  },
  {
    "Country": "Congo (Kinshasa)",
    "Data_Year": 2015,
    "Happiness_Rank": 120,
    "Happiness_Score": 4.52,
    "Life_Expectancy": 62.4,
    "Population": 81400000,
    "Latitude": 4.0383,
    "Longitude": 21.7587
  },
  {
    "Country": "Qatar",
    "Data_Year": 2019,
    "Happiness_Rank": 32,
    "Happiness_Score": 6.37,
    "Life_Expectancy": 80.5,
    "Population": 2830000,
    "Latitude": 25.354826,
    "Longitude": 51.183884
  },
  {
    "Country": "Congo (Kinshasa)",
    "Data_Year": 2017,
    "Happiness_Rank": 126,
    "Happiness_Score": 4.28,
    "Life_Expectancy": 63,
    "Population": 86800000,
    "Latitude": 4.0383,
    "Longitude": 21.7587
  },
  {
    "Country": "Costa Rica",
    "Data_Year": 2016,
    "Happiness_Rank": 14,
    "Happiness_Score": 7.09,
    "Life_Expectancy": 79.5,
    "Population": 4900000,
    "Latitude": 9.7489,
    "Longitude": -83.7534
  },
  {
    "Country": "Colombia",
    "Data_Year": 2019,
    "Happiness_Rank": 37,
    "Happiness_Score": 6.26,
    "Life_Expectancy": 80.5,
    "Population": 50300000,
    "Latitude": 4.570868,
    "Longitude": -74.297333
  },
  {
    "Country": "Costa Rica",
    "Data_Year": 2018,
    "Happiness_Rank": 13,
    "Happiness_Score": 7.07,
    "Life_Expectancy": 79.7,
    "Population": 5000000,
    "Latitude": 9.7489,
    "Longitude": -83.7534
  },
  {
    "Country": "Costa Rica",
    "Data_Year": 2017,
    "Happiness_Rank": 12,
    "Happiness_Score": 7.08,
    "Life_Expectancy": 79.5,
    "Population": 4950000,
    "Latitude": 9.7489,
    "Longitude": -83.7534
  },
  {
    "Country": "Costa Rica",
    "Data_Year": 2015,
    "Happiness_Rank": 12,
    "Happiness_Score": 7.23,
    "Life_Expectancy": 79.9,
    "Population": 4850000,
    "Latitude": 9.7489,
    "Longitude": -83.7534
  },
  {
    "Country": "Croatia",
    "Data_Year": 2016,
    "Happiness_Rank": 74,
    "Happiness_Score": 5.49,
    "Life_Expectancy": 78.3,
    "Population": 4210000,
    "Latitude": 45.1,
    "Longitude": 15.2
  },
  {
    "Country": "Taiwan",
    "Data_Year": 2019,
    "Happiness_Rank": 26,
    "Happiness_Score": 6.44,
    "Life_Expectancy": 80.19,
    "Population": 23773876,
    "Latitude": 23.69781,
    "Longitude": 120.960515
  },
  {
    "Country": "Croatia",
    "Data_Year": 2018,
    "Happiness_Rank": 82,
    "Happiness_Score": 5.32,
    "Life_Expectancy": 78.7,
    "Population": 4160000,
    "Latitude": 45.1,
    "Longitude": 15.2
  },
  {
    "Country": "Croatia",
    "Data_Year": 2017,
    "Happiness_Rank": 77,
    "Happiness_Score": 5.29,
    "Life_Expectancy": 78.5,
    "Population": 4180000,
    "Latitude": 45.1,
    "Longitude": 15.2
  },
  {
    "Country": "Croatia",
    "Data_Year": 2015,
    "Happiness_Rank": 62,
    "Happiness_Score": 5.76,
    "Life_Expectancy": 77.6,
    "Population": 4230000,
    "Latitude": 45.1,
    "Longitude": 15.2
  },
  {
    "Country": "Chile",
    "Data_Year": 2019,
    "Happiness_Rank": 25,
    "Happiness_Score": 6.48,
    "Life_Expectancy": 80,
    "Population": 19000000,
    "Latitude": -35.675147,
    "Longitude": -71.542969
  },
  {
    "Country": "Cyprus",
    "Data_Year": 2017,
    "Happiness_Rank": 65,
    "Happiness_Score": 5.62,
    "Life_Expectancy": 81.7,
    "Population": 1180000,
    "Latitude": 35.126413,
    "Longitude": 33.429859
  },
  {
    "Country": "Cyprus",
    "Data_Year": 2015,
    "Happiness_Rank": 67,
    "Happiness_Score": 5.69,
    "Life_Expectancy": 81.5,
    "Population": 1160000,
    "Latitude": 35.126413,
    "Longitude": 33.429859
  },
  {
    "Country": "Cyprus",
    "Data_Year": 2016,
    "Happiness_Rank": 69,
    "Happiness_Score": 5.55,
    "Life_Expectancy": 81.7,
    "Population": 1170000,
    "Latitude": 35.126413,
    "Longitude": 33.429859
  },
  {
    "Country": "Cyprus",
    "Data_Year": 2018,
    "Happiness_Rank": 61,
    "Happiness_Score": 5.76,
    "Life_Expectancy": 81.9,
    "Population": 1190000,
    "Latitude": 35.126413,
    "Longitude": 33.429859
  },
  {
    "Country": "Czech Republic",
    "Data_Year": 2017,
    "Happiness_Rank": 23,
    "Happiness_Score": 6.61,
    "Life_Expectancy": 79.2,
    "Population": 10600000,
    "Latitude": 49.8175,
    "Longitude": 15.473
  },
  {
    "Country": "Czech Republic",
    "Data_Year": 2016,
    "Happiness_Rank": 27,
    "Happiness_Score": 6.6,
    "Life_Expectancy": 79,
    "Population": 10600000,
    "Latitude": 49.8175,
    "Longitude": 15.473
  },
  {
    "Country": "Czech Republic",
    "Data_Year": 2018,
    "Happiness_Rank": 21,
    "Happiness_Score": 6.71,
    "Life_Expectancy": 79.3,
    "Population": 10700000,
    "Latitude": 49.8175,
    "Longitude": 15.473
  },
  {
    "Country": "Costa Rica",
    "Data_Year": 2019,
    "Happiness_Rank": 13,
    "Happiness_Score": 7.07,
    "Life_Expectancy": 79.8,
    "Population": 5050000,
    "Latitude": 9.7489,
    "Longitude": -83.7534
  },
  {
    "Country": "Czech Republic",
    "Data_Year": 2015,
    "Happiness_Rank": 31,
    "Happiness_Score": 6.5,
    "Life_Expectancy": 78.8,
    "Population": 10600000,
    "Latitude": 49.8175,
    "Longitude": 15.473
  },
  {
    "Country": "Denmark",
    "Data_Year": 2018,
    "Happiness_Rank": 3,
    "Happiness_Score": 7.56,
    "Life_Expectancy": 80.9,
    "Population": 5750000,
    "Latitude": 56.26392,
    "Longitude": 9.501785
  },
  {
    "Country": "Denmark",
    "Data_Year": 2017,
    "Happiness_Rank": 2,
    "Happiness_Score": 7.52,
    "Life_Expectancy": 80.8,
    "Population": 5730000,
    "Latitude": 56.26392,
    "Longitude": 9.501785
  },
  {
    "Country": "Denmark",
    "Data_Year": 2016,
    "Happiness_Rank": 1,
    "Happiness_Score": 7.53,
    "Life_Expectancy": 80.8,
    "Population": 5710000,
    "Latitude": 56.26392,
    "Longitude": 9.501785
  },
  {
    "Country": "Bahrain",
    "Data_Year": 2019,
    "Happiness_Rank": 43,
    "Happiness_Score": 6.1,
    "Life_Expectancy": 79.8,
    "Population": 1640000,
    "Latitude": 25.930414,
    "Longitude": 50.637772
  },
  {
    "Country": "Denmark",
    "Data_Year": 2015,
    "Happiness_Rank": 3,
    "Happiness_Score": 7.53,
    "Life_Expectancy": 80.9,
    "Population": 5690000,
    "Latitude": 56.26392,
    "Longitude": 9.501785
  },
  {
    "Country": "Djibouti",
    "Data_Year": 2015,
    "Happiness_Rank": 126,
    "Happiness_Score": 4.37,
    "Life_Expectancy": 66.3,
    "Population": 914000,
    "Latitude": 11.825138,
    "Longitude": 42.590275
  },
  {
    "Country": "Panama",
    "Data_Year": 2019,
    "Happiness_Rank": 27,
    "Happiness_Score": 6.43,
    "Life_Expectancy": 79.7,
    "Population": 4250000,
    "Latitude": 8.537981,
    "Longitude": -80.782127
  },
  {
    "Country": "Dominican Republic",
    "Data_Year": 2015,
    "Happiness_Rank": 98,
    "Happiness_Score": 4.88,
    "Life_Expectancy": 72.8,
    "Population": 10300000,
    "Latitude": 18.7357,
    "Longitude": -70.1627
  },
  {
    "Country": "Dominican Republic",
    "Data_Year": 2018,
    "Happiness_Rank": 83,
    "Happiness_Score": 5.3,
    "Life_Expectancy": 73.3,
    "Population": 10600000,
    "Latitude": 18.7357,
    "Longitude": -70.1627
  },
  {
    "Country": "Dominican Republic",
    "Data_Year": 2017,
    "Happiness_Rank": 86,
    "Happiness_Score": 5.23,
    "Life_Expectancy": 73.1,
    "Population": 10500000,
    "Latitude": 18.7357,
    "Longitude": -70.1627
  },
  {
    "Country": "Dominican Republic",
    "Data_Year": 2016,
    "Happiness_Rank": 89,
    "Happiness_Score": 5.16,
    "Life_Expectancy": 72.8,
    "Population": 10400000,
    "Latitude": 18.7357,
    "Longitude": -70.1627
  },
  {
    "Country": "Ecuador",
    "Data_Year": 2016,
    "Happiness_Rank": 51,
    "Happiness_Score": 5.98,
    "Life_Expectancy": 76.5,
    "Population": 16500000,
    "Latitude": -1.831239,
    "Longitude": -78.183406
  },
  {
    "Country": "Ecuador",
    "Data_Year": 2017,
    "Happiness_Rank": 44,
    "Happiness_Score": 6.01,
    "Life_Expectancy": 76.7,
    "Population": 16800000,
    "Latitude": -1.831239,
    "Longitude": -78.183406
  },
  {
    "Country": "Ecuador",
    "Data_Year": 2015,
    "Happiness_Rank": 48,
    "Happiness_Score": 5.98,
    "Life_Expectancy": 76.6,
    "Population": 16200000,
    "Latitude": -1.831239,
    "Longitude": -78.183406
  },
  {
    "Country": "Ecuador",
    "Data_Year": 2018,
    "Happiness_Rank": 48,
    "Happiness_Score": 5.97,
    "Life_Expectancy": 77,
    "Population": 17100000,
    "Latitude": -1.831239,
    "Longitude": -78.183406
  },
  {
    "Country": "Jordan",
    "Data_Year": 2019,
    "Happiness_Rank": 90,
    "Happiness_Score": 5.16,
    "Life_Expectancy": 79.6,
    "Population": 10100000,
    "Latitude": 30.585164,
    "Longitude": 36.238414
  },
  {
    "Country": "Egypt",
    "Data_Year": 2018,
    "Happiness_Rank": 122,
    "Happiness_Score": 4.42,
    "Life_Expectancy": 70.8,
    "Population": 98400000,
    "Latitude": 26.820553,
    "Longitude": 30.802498
  },
  {
    "Country": "Czech Republic",
    "Data_Year": 2019,
    "Happiness_Rank": 21,
    "Happiness_Score": 6.71,
    "Life_Expectancy": 79.5,
    "Population": 10700000,
    "Latitude": 49.8175,
    "Longitude": 15.473
  },
  {
    "Country": "Egypt",
    "Data_Year": 2016,
    "Happiness_Rank": 120,
    "Happiness_Score": 4.36,
    "Life_Expectancy": 70.5,
    "Population": 94400000,
    "Latitude": 26.820553,
    "Longitude": 30.802498
  },
  {
    "Country": "Egypt",
    "Data_Year": 2015,
    "Happiness_Rank": 135,
    "Happiness_Score": 4.19,
    "Life_Expectancy": 70.2,
    "Population": 92400000,
    "Latitude": 26.820553,
    "Longitude": 30.802498
  },
  {
    "Country": "Egypt",
    "Data_Year": 2017,
    "Happiness_Rank": 104,
    "Happiness_Score": 4.74,
    "Life_Expectancy": 70.6,
    "Population": 96400000,
    "Latitude": 26.820553,
    "Longitude": 30.802498
  },
  {
    "Country": "El Salvador",
    "Data_Year": 2018,
    "Happiness_Rank": 40,
    "Happiness_Score": 6.17,
    "Life_Expectancy": 74.2,
    "Population": 6420000,
    "Latitude": 13.7942,
    "Longitude": -88.8965
  },
  {
    "Country": "El Salvador",
    "Data_Year": 2016,
    "Happiness_Rank": 46,
    "Happiness_Score": 6.07,
    "Life_Expectancy": 73.8,
    "Population": 6360000,
    "Latitude": 13.7942,
    "Longitude": -88.8965
  },
  {
    "Country": "El Salvador",
    "Data_Year": 2017,
    "Happiness_Rank": 45,
    "Happiness_Score": 6,
    "Life_Expectancy": 74,
    "Population": 6390000,
    "Latitude": 13.7942,
    "Longitude": -88.8965
  },
  {
    "Country": "Turkey",
    "Data_Year": 2019,
    "Happiness_Rank": 74,
    "Happiness_Score": 5.48,
    "Life_Expectancy": 79.5,
    "Population": 83400000,
    "Latitude": 38.963745,
    "Longitude": 35.243322
  },
  {
    "Country": "El Salvador",
    "Data_Year": 2015,
    "Happiness_Rank": 42,
    "Happiness_Score": 6.13,
    "Life_Expectancy": 72.1,
    "Population": 6330000,
    "Latitude": 13.7942,
    "Longitude": -88.8965
  },
  {
    "Country": "Estonia",
    "Data_Year": 2015,
    "Happiness_Rank": 73,
    "Happiness_Score": 5.43,
    "Life_Expectancy": 77.7,
    "Population": 1320000,
    "Latitude": 58.595272,
    "Longitude": 25.013607
  },
  {
    "Country": "Estonia",
    "Data_Year": 2017,
    "Happiness_Rank": 66,
    "Happiness_Score": 5.61,
    "Life_Expectancy": 78.1,
    "Population": 1320000,
    "Latitude": 58.595272,
    "Longitude": 25.013607
  },
  {
    "Country": "Estonia",
    "Data_Year": 2016,
    "Happiness_Rank": 72,
    "Happiness_Score": 5.52,
    "Life_Expectancy": 77.9,
    "Population": 1320000,
    "Latitude": 58.595272,
    "Longitude": 25.013607
  },
  {
    "Country": "Estonia",
    "Data_Year": 2018,
    "Happiness_Rank": 63,
    "Happiness_Score": 5.74,
    "Life_Expectancy": 78.3,
    "Population": 1320000,
    "Latitude": 58.595272,
    "Longitude": 25.013607
  },
  {
    "Country": "Nicaragua",
    "Data_Year": 2019,
    "Happiness_Rank": 41,
    "Happiness_Score": 6.14,
    "Life_Expectancy": 79.2,
    "Population": 6550000,
    "Latitude": 12.865416,
    "Longitude": -85.207229
  },
  {
    "Country": "Ethiopia",
    "Data_Year": 2018,
    "Happiness_Rank": 127,
    "Happiness_Score": 4.35,
    "Life_Expectancy": 68.8,
    "Population": 109000000,
    "Latitude": 9.145,
    "Longitude": 40.489673
  },
  {
    "Country": "Croatia",
    "Data_Year": 2019,
    "Happiness_Rank": 82,
    "Happiness_Score": 5.32,
    "Life_Expectancy": 78.8,
    "Population": 4130000,
    "Latitude": 45.1,
    "Longitude": 15.2
  },
  {
    "Country": "Ethiopia",
    "Data_Year": 2017,
    "Happiness_Rank": 119,
    "Happiness_Score": 4.46,
    "Life_Expectancy": 68.4,
    "Population": 106000000,
    "Latitude": 9.145,
    "Longitude": 40.489673
  },
  {
    "Country": "Ethiopia",
    "Data_Year": 2016,
    "Happiness_Rank": 115,
    "Happiness_Score": 4.51,
    "Life_Expectancy": 67.8,
    "Population": 104000000,
    "Latitude": 9.145,
    "Longitude": 40.489673
  },
  {
    "Country": "Ethiopia",
    "Data_Year": 2015,
    "Happiness_Rank": 122,
    "Happiness_Score": 4.51,
    "Life_Expectancy": 67.2,
    "Population": 101000000,
    "Latitude": 9.145,
    "Longitude": 40.489673
  },
  {
    "Country": "Tunisia",
    "Data_Year": 2019,
    "Happiness_Rank": 111,
    "Happiness_Score": 4.59,
    "Life_Expectancy": 78.7,
    "Population": 11700000,
    "Latitude": 33.886917,
    "Longitude": 9.537499
  },
  {
    "Country": "Finland",
    "Data_Year": 2018,
    "Happiness_Rank": 1,
    "Happiness_Score": 7.63,
    "Life_Expectancy": 81.6,
    "Population": 5520000,
    "Latitude": 61.92411,
    "Longitude": 25.748151
  },
  {
    "Country": "Finland",
    "Data_Year": 2016,
    "Happiness_Rank": 5,
    "Happiness_Score": 7.41,
    "Life_Expectancy": 81.5,
    "Population": 5500000,
    "Latitude": 61.92411,
    "Longitude": 25.748151
  },
  {
    "Country": "Finland",
    "Data_Year": 2015,
    "Happiness_Rank": 6,
    "Happiness_Score": 7.41,
    "Life_Expectancy": 81.6,
    "Population": 5480000,
    "Latitude": 61.92411,
    "Longitude": 25.748151
  },
  {
    "Country": "Finland",
    "Data_Year": 2017,
    "Happiness_Rank": 5,
    "Happiness_Score": 7.47,
    "Life_Expectancy": 81.4,
    "Population": 5510000,
    "Latitude": 61.92411,
    "Longitude": 25.748151
  },
  {
    "Country": "France",
    "Data_Year": 2015,
    "Happiness_Rank": 29,
    "Happiness_Score": 6.58,
    "Life_Expectancy": 82.5,
    "Population": 64500000,
    "Latitude": 46.227638,
    "Longitude": 2.213749
  },
  {
    "Country": "United States",
    "Data_Year": 2019,
    "Happiness_Rank": 18,
    "Happiness_Score": 6.89,
    "Life_Expectancy": 78.6,
    "Population": 329000000,
    "Latitude": 37.0902,
    "Longitude": -95.7129
  },
  {
    "Country": "France",
    "Data_Year": 2016,
    "Happiness_Rank": 32,
    "Happiness_Score": 6.48,
    "Life_Expectancy": 82.8,
    "Population": 64700000,
    "Latitude": 46.227638,
    "Longitude": 2.213749
  },
  {
    "Country": "France",
    "Data_Year": 2017,
    "Happiness_Rank": 31,
    "Happiness_Score": 6.44,
    "Life_Expectancy": 82.8,
    "Population": 64800000,
    "Latitude": 46.227638,
    "Longitude": 2.213749
  },
  {
    "Country": "France",
    "Data_Year": 2018,
    "Happiness_Rank": 23,
    "Happiness_Score": 6.49,
    "Life_Expectancy": 83,
    "Population": 65000000,
    "Latitude": 46.227638,
    "Longitude": 2.213749
  },
  {
    "Country": "Thailand",
    "Data_Year": 2019,
    "Happiness_Rank": 46,
    "Happiness_Score": 6.07,
    "Life_Expectancy": 78.6,
    "Population": 69600000,
    "Latitude": 15.870032,
    "Longitude": 100.992541
  },
  {
    "Country": "Gabon",
    "Data_Year": 2018,
    "Happiness_Rank": 103,
    "Happiness_Score": 4.76,
    "Life_Expectancy": 68.8,
    "Population": 2120000,
    "Latitude": -0.803689,
    "Longitude": 11.609444
  },
  {
    "Country": "Gabon",
    "Data_Year": 2015,
    "Happiness_Rank": 143,
    "Happiness_Score": 3.9,
    "Life_Expectancy": 67,
    "Population": 1950000,
    "Latitude": -0.803689,
    "Longitude": 11.609444
  },
  {
    "Country": "Gabon",
    "Data_Year": 2016,
    "Happiness_Rank": 134,
    "Happiness_Score": 4.12,
    "Life_Expectancy": 67.7,
    "Population": 2010000,
    "Latitude": -0.803689,
    "Longitude": 11.609444
  },
  {
    "Country": "Gabon",
    "Data_Year": 2017,
    "Happiness_Rank": 118,
    "Happiness_Score": 4.47,
    "Life_Expectancy": 68.4,
    "Population": 2060000,
    "Latitude": -0.803689,
    "Longitude": 11.609444
  },
  {
    "Country": "Georgia",
    "Data_Year": 2018,
    "Happiness_Rank": 128,
    "Happiness_Score": 4.34,
    "Life_Expectancy": 73,
    "Population": 4000000,
    "Latitude": 42.315407,
    "Longitude": 43.356892
  },
  {
    "Country": "Georgia",
    "Data_Year": 2016,
    "Happiness_Rank": 126,
    "Happiness_Score": 4.25,
    "Life_Expectancy": 72.8,
    "Population": 4020000,
    "Latitude": 42.315407,
    "Longitude": 43.356892
  },
  {
    "Country": "Estonia",
    "Data_Year": 2019,
    "Happiness_Rank": 63,
    "Happiness_Score": 5.74,
    "Life_Expectancy": 78.5,
    "Population": 1330000,
    "Latitude": 58.595272,
    "Longitude": 25.013607
  },
  {
    "Country": "Georgia",
    "Data_Year": 2017,
    "Happiness_Rank": 125,
    "Happiness_Score": 4.29,
    "Life_Expectancy": 72.8,
    "Population": 4010000,
    "Latitude": 42.315407,
    "Longitude": 43.356892
  },
  {
    "Country": "Georgia",
    "Data_Year": 2015,
    "Happiness_Rank": 130,
    "Happiness_Score": 4.3,
    "Life_Expectancy": 73,
    "Population": 4020000,
    "Latitude": 42.315407,
    "Longitude": 43.356892
  },
  {
    "Country": "Germany",
    "Data_Year": 2016,
    "Happiness_Rank": 16,
    "Happiness_Score": 6.99,
    "Life_Expectancy": 80.5,
    "Population": 82200000,
    "Latitude": 51.165691,
    "Longitude": 10.451526
  },
  {
    "Country": "Albania",
    "Data_Year": 2019,
    "Happiness_Rank": 112,
    "Happiness_Score": 4.59,
    "Life_Expectancy": 78.5,
    "Population": 2880000,
    "Latitude": 41.153332,
    "Longitude": 20.168331
  },
  {
    "Country": "Germany",
    "Data_Year": 2018,
    "Happiness_Rank": 15,
    "Happiness_Score": 6.96,
    "Life_Expectancy": 80.8,
    "Population": 83100000,
    "Latitude": 51.165691,
    "Longitude": 10.451526
  },
  {
    "Country": "Germany",
    "Data_Year": 2017,
    "Happiness_Rank": 16,
    "Happiness_Score": 6.95,
    "Life_Expectancy": 80.6,
    "Population": 82700000,
    "Latitude": 51.165691,
    "Longitude": 10.451526
  },
  {
    "Country": "Germany",
    "Data_Year": 2015,
    "Happiness_Rank": 26,
    "Happiness_Score": 6.75,
    "Life_Expectancy": 80.7,
    "Population": 81800000,
    "Latitude": 51.165691,
    "Longitude": 10.451526
  },
  {
    "Country": "Ghana",
    "Data_Year": 2018,
    "Happiness_Rank": 108,
    "Happiness_Score": 4.66,
    "Life_Expectancy": 65.8,
    "Population": 29800000,
    "Latitude": 7.946527,
    "Longitude": -1.023194
  },
  {
    "Country": "Ghana",
    "Data_Year": 2016,
    "Happiness_Rank": 124,
    "Happiness_Score": 4.28,
    "Life_Expectancy": 64.8,
    "Population": 28500000,
    "Latitude": 7.946527,
    "Longitude": -1.023194
  },
  {
    "Country": "Poland",
    "Data_Year": 2019,
    "Happiness_Rank": 42,
    "Happiness_Score": 6.12,
    "Life_Expectancy": 78.4,
    "Population": 37900000,
    "Latitude": 51.919438,
    "Longitude": 19.145136
  },
  {
    "Country": "Ghana",
    "Data_Year": 2015,
    "Happiness_Rank": 114,
    "Happiness_Score": 4.63,
    "Life_Expectancy": 64.4,
    "Population": 27800000,
    "Latitude": 7.946527,
    "Longitude": -1.023194
  },
  {
    "Country": "Ghana",
    "Data_Year": 2017,
    "Happiness_Rank": 131,
    "Happiness_Score": 4.12,
    "Life_Expectancy": 65.5,
    "Population": 29100000,
    "Latitude": 7.946527,
    "Longitude": -1.023194
  },
  {
    "Country": "Greece",
    "Data_Year": 2017,
    "Happiness_Rank": 87,
    "Happiness_Score": 5.23,
    "Life_Expectancy": 81,
    "Population": 10600000,
    "Latitude": 39.074208,
    "Longitude": 21.824312
  },
  {
    "Country": "Greece",
    "Data_Year": 2016,
    "Happiness_Rank": 99,
    "Happiness_Score": 5.03,
    "Life_Expectancy": 80.9,
    "Population": 10600000,
    "Latitude": 39.074208,
    "Longitude": 21.824312
  },
  {
    "Country": "Greece",
    "Data_Year": 2015,
    "Happiness_Rank": 102,
    "Happiness_Score": 4.86,
    "Life_Expectancy": 80.8,
    "Population": 10700000,
    "Latitude": 39.074208,
    "Longitude": 21.824312
  },
  {
    "Country": "Lebanon",
    "Data_Year": 2019,
    "Happiness_Rank": 80,
    "Happiness_Score": 5.36,
    "Life_Expectancy": 78.1,
    "Population": 6860000,
    "Latitude": 33.854721,
    "Longitude": 35.862285
  },
  {
    "Country": "Greece",
    "Data_Year": 2018,
    "Happiness_Rank": 79,
    "Happiness_Score": 5.36,
    "Life_Expectancy": 81.2,
    "Population": 10500000,
    "Latitude": 39.074208,
    "Longitude": 21.824312
  },
  {
    "Country": "Guatemala",
    "Data_Year": 2016,
    "Happiness_Rank": 39,
    "Happiness_Score": 6.32,
    "Life_Expectancy": 72.6,
    "Population": 16600000,
    "Latitude": 15.783471,
    "Longitude": -90.230759
  },
  {
    "Country": "Guatemala",
    "Data_Year": 2018,
    "Happiness_Rank": 30,
    "Happiness_Score": 6.38,
    "Life_Expectancy": 72.9,
    "Population": 17200000,
    "Latitude": 15.783471,
    "Longitude": -90.230759
  },
  {
    "Country": "Algeria",
    "Data_Year": 2019,
    "Happiness_Rank": 84,
    "Happiness_Score": 5.3,
    "Life_Expectancy": 78.1,
    "Population": 43100000,
    "Latitude": 28.033886,
    "Longitude": 1.659626
  },
  {
    "Country": "Guatemala",
    "Data_Year": 2015,
    "Happiness_Rank": 43,
    "Happiness_Score": 6.12,
    "Life_Expectancy": 72.9,
    "Population": 16300000,
    "Latitude": 15.783471,
    "Longitude": -90.230759
  },
  {
    "Country": "Guatemala",
    "Data_Year": 2017,
    "Happiness_Rank": 29,
    "Happiness_Score": 6.45,
    "Life_Expectancy": 72.6,
    "Population": 16900000,
    "Latitude": 15.783471,
    "Longitude": -90.230759
  },
  {
    "Country": "Guinea",
    "Data_Year": 2015,
    "Happiness_Rank": 150,
    "Happiness_Score": 3.66,
    "Life_Expectancy": 59.2,
    "Population": 11400000,
    "Latitude": 9.945587,
    "Longitude": -9.696645
  },
  {
    "Country": "Guinea",
    "Data_Year": 2017,
    "Happiness_Rank": 149,
    "Happiness_Score": 3.51,
    "Life_Expectancy": 60.7,
    "Population": 12100000,
    "Latitude": 9.945587,
    "Longitude": -9.696645
  },
  {
    "Country": "Guinea",
    "Data_Year": 2016,
    "Happiness_Rank": 151,
    "Happiness_Score": 3.61,
    "Life_Expectancy": 60.1,
    "Population": 11700000,
    "Latitude": 9.945587,
    "Longitude": -9.696645
  },
  {
    "Country": "Iran",
    "Data_Year": 2019,
    "Happiness_Rank": 106,
    "Happiness_Score": 4.71,
    "Life_Expectancy": 77.8,
    "Population": 82900000,
    "Latitude": 32.427908,
    "Longitude": 53.688046
  },
  {
    "Country": "Guinea",
    "Data_Year": 2018,
    "Happiness_Rank": 140,
    "Happiness_Score": 3.96,
    "Life_Expectancy": 61.2,
    "Population": 12400000,
    "Latitude": 9.945587,
    "Longitude": -9.696645
  },
  {
    "Country": "Haiti",
    "Data_Year": 2015,
    "Happiness_Rank": 119,
    "Happiness_Score": 4.52,
    "Life_Expectancy": 64,
    "Population": 10700000,
    "Latitude": 18.971187,
    "Longitude": -72.285215
  },
  {
    "Country": "Haiti",
    "Data_Year": 2018,
    "Happiness_Rank": 148,
    "Happiness_Score": 3.58,
    "Life_Expectancy": 65.3,
    "Population": 11100000,
    "Latitude": 18.971187,
    "Longitude": -72.285215
  },
  {
    "Country": "Haiti",
    "Data_Year": 2017,
    "Happiness_Rank": 145,
    "Happiness_Score": 3.6,
    "Life_Expectancy": 65,
    "Population": 11000000,
    "Latitude": 18.971187,
    "Longitude": -72.285215
  },
  {
    "Country": "Haiti",
    "Data_Year": 2016,
    "Happiness_Rank": 136,
    "Happiness_Score": 4.03,
    "Life_Expectancy": 64.3,
    "Population": 10800000,
    "Latitude": 18.971187,
    "Longitude": -72.285215
  },
  {
    "Country": "Sri Lanka",
    "Data_Year": 2019,
    "Happiness_Rank": 116,
    "Happiness_Score": 4.47,
    "Life_Expectancy": 77.8,
    "Population": 21300000,
    "Latitude": 7.8731,
    "Longitude": 80.7718
  },
  {
    "Country": "Honduras",
    "Data_Year": 2017,
    "Happiness_Rank": 91,
    "Happiness_Score": 5.18,
    "Life_Expectancy": 74,
    "Population": 9430000,
    "Latitude": 15.199999,
    "Longitude": -86.241905
  },
  {
    "Country": "Honduras",
    "Data_Year": 2016,
    "Happiness_Rank": 104,
    "Happiness_Score": 4.87,
    "Life_Expectancy": 73.8,
    "Population": 9270000,
    "Latitude": 15.199999,
    "Longitude": -86.241905
  },
  {
    "Country": "Slovakia",
    "Data_Year": 2019,
    "Happiness_Rank": 39,
    "Happiness_Score": 6.17,
    "Life_Expectancy": 77.54,
    "Population": 5457013,
    "Latitude": 48.669026,
    "Longitude": 19.699024
  },
  {
    "Country": "Honduras",
    "Data_Year": 2018,
    "Happiness_Rank": 72,
    "Happiness_Score": 5.5,
    "Life_Expectancy": 74.2,
    "Population": 9590000,
    "Latitude": 15.199999,
    "Longitude": -86.241905
  },
  {
    "Country": "Honduras",
    "Data_Year": 2015,
    "Happiness_Rank": 105,
    "Happiness_Score": 4.79,
    "Life_Expectancy": 72.1,
    "Population": 9110000,
    "Latitude": 15.199999,
    "Longitude": -86.241905
  },
  {
    "Country": "Hong Kong",
    "Data_Year": 2015,
    "Happiness_Rank": 72,
    "Happiness_Score": 5.47,
    "Life_Expectancy": 83.89,
    "Population": 7185996,
    "Latitude": 22.3193,
    "Longitude": 114.1694
  },
  {
    "Country": "Hong Kong",
    "Data_Year": 2018,
    "Happiness_Rank": 76,
    "Happiness_Score": 5.43,
    "Life_Expectancy": 84.63,
    "Population": 7371730,
    "Latitude": 22.3193,
    "Longitude": 114.1694
  },
  {
    "Country": "China",
    "Data_Year": 2019,
    "Happiness_Rank": 86,
    "Happiness_Score": 5.25,
    "Life_Expectancy": 77.5,
    "Population": 1430000000,
    "Latitude": 35.86166,
    "Longitude": 104.195397
  },
  {
    "Country": "Hong Kong",
    "Data_Year": 2016,
    "Happiness_Rank": 75,
    "Happiness_Score": 5.46,
    "Life_Expectancy": 84.14,
    "Population": 7243542,
    "Latitude": 22.3193,
    "Longitude": 114.1694
  },
  {
    "Country": "Hong Kong",
    "Data_Year": 2017,
    "Happiness_Rank": 71,
    "Happiness_Score": 5.47,
    "Life_Expectancy": 84.38,
    "Population": 7306322,
    "Latitude": 22.3193,
    "Longitude": 114.1694
  },
  {
    "Country": "Hungary",
    "Data_Year": 2017,
    "Happiness_Rank": 75,
    "Happiness_Score": 5.32,
    "Life_Expectancy": 76.8,
    "Population": 9730000,
    "Latitude": 47.162494,
    "Longitude": 19.503304
  },
  {
    "Country": "Uruguay",
    "Data_Year": 2019,
    "Happiness_Rank": 31,
    "Happiness_Score": 6.38,
    "Life_Expectancy": 77.3,
    "Population": 3460000,
    "Latitude": -32.522779,
    "Longitude": -55.765835
  },
  {
    "Country": "Hungary",
    "Data_Year": 2018,
    "Happiness_Rank": 69,
    "Happiness_Score": 5.62,
    "Life_Expectancy": 77,
    "Population": 9710000,
    "Latitude": 47.162494,
    "Longitude": 19.503304
  },
  {
    "Country": "Hungary",
    "Data_Year": 2016,
    "Happiness_Rank": 91,
    "Happiness_Score": 5.14,
    "Life_Expectancy": 76.4,
    "Population": 9750000,
    "Latitude": 47.162494,
    "Longitude": 19.503304
  },
  {
    "Country": "Hungary",
    "Data_Year": 2015,
    "Happiness_Rank": 104,
    "Happiness_Score": 4.8,
    "Life_Expectancy": 75.5,
    "Population": 9780000,
    "Latitude": 47.162494,
    "Longitude": 19.503304
  },
  {
    "Country": "Iceland",
    "Data_Year": 2018,
    "Happiness_Rank": 4,
    "Happiness_Score": 7.5,
    "Life_Expectancy": 82.9,
    "Population": 337000,
    "Latitude": 64.963051,
    "Longitude": -19.020835
  },
  {
    "Country": "Iceland",
    "Data_Year": 2016,
    "Happiness_Rank": 3,
    "Happiness_Score": 7.5,
    "Life_Expectancy": 82.7,
    "Population": 332000,
    "Latitude": 64.963051,
    "Longitude": -19.020835
  },
  {
    "Country": "Iceland",
    "Data_Year": 2015,
    "Happiness_Rank": 2,
    "Happiness_Score": 7.56,
    "Life_Expectancy": 82.7,
    "Population": 330000,
    "Latitude": 64.963051,
    "Longitude": -19.020835
  },
  {
    "Country": "Iceland",
    "Data_Year": 2017,
    "Happiness_Rank": 3,
    "Happiness_Score": 7.5,
    "Life_Expectancy": 82.8,
    "Population": 334000,
    "Latitude": 64.963051,
    "Longitude": -19.020835
  },
  {
    "Country": "Ecuador",
    "Data_Year": 2019,
    "Happiness_Rank": 48,
    "Happiness_Score": 5.97,
    "Life_Expectancy": 77.2,
    "Population": 17400000,
    "Latitude": -1.831239,
    "Longitude": -78.183406
  },
  {
    "Country": "India",
    "Data_Year": 2016,
    "Happiness_Rank": 118,
    "Happiness_Score": 4.4,
    "Life_Expectancy": 68.6,
    "Population": 1320000000,
    "Latitude": 20.593684,
    "Longitude": 78.96288
  },
  {
    "Country": "Hungary",
    "Data_Year": 2019,
    "Happiness_Rank": 69,
    "Happiness_Score": 5.62,
    "Life_Expectancy": 77.2,
    "Population": 9680000,
    "Latitude": 47.162494,
    "Longitude": 19.503304
  },
  {
    "Country": "India",
    "Data_Year": 2015,
    "Happiness_Rank": 117,
    "Happiness_Score": 4.57,
    "Life_Expectancy": 68.4,
    "Population": 1310000000,
    "Latitude": 20.593684,
    "Longitude": 78.96288
  },
  {
    "Country": "India",
    "Data_Year": 2017,
    "Happiness_Rank": 122,
    "Happiness_Score": 4.32,
    "Life_Expectancy": 69,
    "Population": 1340000000,
    "Latitude": 20.593684,
    "Longitude": 78.96288
  },
  {
    "Country": "India",
    "Data_Year": 2018,
    "Happiness_Rank": 133,
    "Happiness_Score": 4.19,
    "Life_Expectancy": 69.2,
    "Population": 1350000000,
    "Latitude": 20.593684,
    "Longitude": 78.96288
  },
  {
    "Country": "Indonesia",
    "Data_Year": 2015,
    "Happiness_Rank": 74,
    "Happiness_Score": 5.4,
    "Life_Expectancy": 71,
    "Population": 258000000,
    "Latitude": -0.789275,
    "Longitude": 113.921327
  },
  {
    "Country": "Indonesia",
    "Data_Year": 2016,
    "Happiness_Rank": 79,
    "Happiness_Score": 5.31,
    "Life_Expectancy": 71.2,
    "Population": 262000000,
    "Latitude": -0.789275,
    "Longitude": 113.921327
  },
  {
    "Country": "Indonesia",
    "Data_Year": 2018,
    "Happiness_Rank": 96,
    "Happiness_Score": 5.09,
    "Life_Expectancy": 71.7,
    "Population": 268000000,
    "Latitude": -0.789275,
    "Longitude": 113.921327
  },
  {
    "Country": "Palestinian Territories",
    "Data_Year": 2019,
    "Happiness_Rank": 104,
    "Happiness_Score": 4.74,
    "Life_Expectancy": 77.2,
    "Population": 4980000,
    "Latitude": 31.9522,
    "Longitude": 35.2332
  },
  {
    "Country": "Indonesia",
    "Data_Year": 2017,
    "Happiness_Rank": 81,
    "Happiness_Score": 5.26,
    "Life_Expectancy": 71.5,
    "Population": 265000000,
    "Latitude": -0.789275,
    "Longitude": 113.921327
  },
  {
    "Country": "Iran",
    "Data_Year": 2017,
    "Happiness_Rank": 108,
    "Happiness_Score": 4.69,
    "Life_Expectancy": 77.3,
    "Population": 80700000,
    "Latitude": 32.427908,
    "Longitude": 53.688046
  },
  {
    "Country": "Iran",
    "Data_Year": 2016,
    "Happiness_Rank": 105,
    "Happiness_Score": 4.81,
    "Life_Expectancy": 77,
    "Population": 79600000,
    "Latitude": 32.427908,
    "Longitude": 53.688046
  },
  {
    "Country": "Iran",
    "Data_Year": 2015,
    "Happiness_Rank": 110,
    "Happiness_Score": 4.69,
    "Life_Expectancy": 76.5,
    "Population": 78500000,
    "Latitude": 32.427908,
    "Longitude": 53.688046
  },
  {
    "Country": "Saudi Arabia",
    "Data_Year": 2019,
    "Happiness_Rank": 33,
    "Happiness_Score": 6.37,
    "Life_Expectancy": 77.1,
    "Population": 34300000,
    "Latitude": 23.8859,
    "Longitude": 45.0792
  },
  {
    "Country": "Iran",
    "Data_Year": 2018,
    "Happiness_Rank": 106,
    "Happiness_Score": 4.71,
    "Life_Expectancy": 77.6,
    "Population": 81800000,
    "Latitude": 32.427908,
    "Longitude": 53.688046
  },
  {
    "Country": "Iraq",
    "Data_Year": 2016,
    "Happiness_Rank": 112,
    "Happiness_Score": 4.58,
    "Life_Expectancy": 76.7,
    "Population": 36600000,
    "Latitude": 33.223191,
    "Longitude": 43.679291
  },
  {
    "Country": "Iraq",
    "Data_Year": 2019,
    "Happiness_Rank": 117,
    "Happiness_Score": 4.46,
    "Life_Expectancy": 77.1,
    "Population": 39300000,
    "Latitude": 33.223191,
    "Longitude": 43.679291
  },
  {
    "Country": "Iraq",
    "Data_Year": 2018,
    "Happiness_Rank": 117,
    "Happiness_Score": 4.46,
    "Life_Expectancy": 76.9,
    "Population": 38400000,
    "Latitude": 33.223191,
    "Longitude": 43.679291
  },
  {
    "Country": "Iraq",
    "Data_Year": 2015,
    "Happiness_Rank": 112,
    "Happiness_Score": 4.68,
    "Life_Expectancy": 76.3,
    "Population": 35600000,
    "Latitude": 33.223191,
    "Longitude": 43.679291
  },
  {
    "Country": "Iraq",
    "Data_Year": 2017,
    "Happiness_Rank": 117,
    "Happiness_Score": 4.5,
    "Life_Expectancy": 76.7,
    "Population": 37600000,
    "Latitude": 33.223191,
    "Longitude": 43.679291
  },
  {
    "Country": "Ireland",
    "Data_Year": 2018,
    "Happiness_Rank": 14,
    "Happiness_Score": 6.98,
    "Life_Expectancy": 82.1,
    "Population": 4820000,
    "Latitude": 53.41291,
    "Longitude": -8.24389
  },
  {
    "Country": "Ireland",
    "Data_Year": 2015,
    "Happiness_Rank": 18,
    "Happiness_Score": 6.94,
    "Life_Expectancy": 81.6,
    "Population": 4650000,
    "Latitude": 53.41291,
    "Longitude": -8.24389
  },
  {
    "Country": "Ireland",
    "Data_Year": 2016,
    "Happiness_Rank": 19,
    "Happiness_Score": 6.91,
    "Life_Expectancy": 81.8,
    "Population": 4700000,
    "Latitude": 53.41291,
    "Longitude": -8.24389
  },
  {
    "Country": "Argentina",
    "Data_Year": 2019,
    "Happiness_Rank": 29,
    "Happiness_Score": 6.39,
    "Life_Expectancy": 77,
    "Population": 44800000,
    "Latitude": -38.416097,
    "Longitude": -63.616672
  },
  {
    "Country": "Ireland",
    "Data_Year": 2017,
    "Happiness_Rank": 15,
    "Happiness_Score": 6.98,
    "Life_Expectancy": 81.8,
    "Population": 4750000,
    "Latitude": 53.41291,
    "Longitude": -8.24389
  },
  {
    "Country": "Israel",
    "Data_Year": 2016,
    "Happiness_Rank": 11,
    "Happiness_Score": 7.27,
    "Life_Expectancy": 82.9,
    "Population": 8110000,
    "Latitude": 31.046051,
    "Longitude": 34.851612
  },
  {
    "Country": "Bosnia and Herzegovina",
    "Data_Year": 2019,
    "Happiness_Rank": 93,
    "Happiness_Score": 5.13,
    "Life_Expectancy": 77,
    "Population": 3300000,
    "Latitude": 43.9143,
    "Longitude": 17.6791
  },
  {
    "Country": "Israel",
    "Data_Year": 2017,
    "Happiness_Rank": 11,
    "Happiness_Score": 7.21,
    "Life_Expectancy": 83,
    "Population": 8240000,
    "Latitude": 31.046051,
    "Longitude": 34.851612
  },
  {
    "Country": "Israel",
    "Data_Year": 2015,
    "Happiness_Rank": 11,
    "Happiness_Score": 7.28,
    "Life_Expectancy": 82.6,
    "Population": 7980000,
    "Latitude": 31.046051,
    "Longitude": 34.851612
  },
  {
    "Country": "Israel",
    "Data_Year": 2018,
    "Happiness_Rank": 19,
    "Happiness_Score": 6.81,
    "Life_Expectancy": 83.1,
    "Population": 8380000,
    "Latitude": 31.046051,
    "Longitude": 34.851612
  },
  {
    "Country": "Italy",
    "Data_Year": 2018,
    "Happiness_Rank": 47,
    "Happiness_Score": 6,
    "Life_Expectancy": 83.3,
    "Population": 60600000,
    "Latitude": 41.87194,
    "Longitude": 12.56738
  },
  {
    "Country": "Macedonia",
    "Data_Year": 2019,
    "Happiness_Rank": 89,
    "Happiness_Score": 5.18,
    "Life_Expectancy": 76.85,
    "Population": 2083459,
    "Latitude": 41.6086,
    "Longitude": 21.7453
  },
  {
    "Country": "Italy",
    "Data_Year": 2017,
    "Happiness_Rank": 48,
    "Happiness_Score": 5.96,
    "Life_Expectancy": 83.2,
    "Population": 60700000,
    "Latitude": 41.87194,
    "Longitude": 12.56738
  },
  {
    "Country": "Italy",
    "Data_Year": 2016,
    "Happiness_Rank": 50,
    "Happiness_Score": 5.98,
    "Life_Expectancy": 83,
    "Population": 60700000,
    "Latitude": 41.87194,
    "Longitude": 12.56738
  },
  {
    "Country": "Italy",
    "Data_Year": 2015,
    "Happiness_Rank": 50,
    "Happiness_Score": 5.95,
    "Life_Expectancy": 82.6,
    "Population": 60600000,
    "Latitude": 41.87194,
    "Longitude": 12.56738
  },
  {
    "Country": "Ivory Coast",
    "Data_Year": 2015,
    "Happiness_Rank": 151,
    "Happiness_Score": 3.66,
    "Life_Expectancy": 56.07,
    "Population": 23226143,
    "Latitude": 7.54,
    "Longitude": 5.5471
  },
  {
    "Country": "Montenegro",
    "Data_Year": 2019,
    "Happiness_Rank": 81,
    "Happiness_Score": 5.35,
    "Life_Expectancy": 76.7,
    "Population": 628000,
    "Latitude": 42.708678,
    "Longitude": 19.37439
  },
  {
    "Country": "Ivory Coast",
    "Data_Year": 2018,
    "Happiness_Rank": 107,
    "Happiness_Score": 4.67,
    "Life_Expectancy": 57.02,
    "Population": 25069230,
    "Latitude": 7.54,
    "Longitude": 5.5471
  },
  {
    "Country": "Ivory Coast",
    "Data_Year": 2017,
    "Happiness_Rank": 128,
    "Happiness_Score": 4.18,
    "Life_Expectancy": 57.02,
    "Population": 24437470,
    "Latitude": 7.54,
    "Longitude": 5.5471
  },
  {
    "Country": "Ivory Coast",
    "Data_Year": 2016,
    "Happiness_Rank": 139,
    "Happiness_Score": 3.92,
    "Life_Expectancy": 56.57,
    "Population": 23822714,
    "Latitude": 7.54,
    "Longitude": 5.5471
  },
  {
    "Country": "Jamaica",
    "Data_Year": 2018,
    "Happiness_Rank": 56,
    "Happiness_Score": 5.89,
    "Life_Expectancy": 74.8,
    "Population": 2930000,
    "Latitude": 18.109581,
    "Longitude": -77.297508
  },
  {
    "Country": "Paraguay",
    "Data_Year": 2019,
    "Happiness_Rank": 64,
    "Happiness_Score": 5.68,
    "Life_Expectancy": 76.4,
    "Population": 7040000,
    "Latitude": -23.442503,
    "Longitude": -58.443832
  },
  {
    "Country": "Jamaica",
    "Data_Year": 2017,
    "Happiness_Rank": 76,
    "Happiness_Score": 5.31,
    "Life_Expectancy": 74.7,
    "Population": 2920000,
    "Latitude": 18.109581,
    "Longitude": -77.297508
  },
  {
    "Country": "Jamaica",
    "Data_Year": 2015,
    "Happiness_Rank": 65,
    "Happiness_Score": 5.71,
    "Life_Expectancy": 74.6,
    "Population": 2890000,
    "Latitude": 18.109581,
    "Longitude": -77.297508
  },
  {
    "Country": "Jamaica",
    "Data_Year": 2016,
    "Happiness_Rank": 73,
    "Happiness_Score": 5.51,
    "Life_Expectancy": 74.5,
    "Population": 2910000,
    "Latitude": 18.109581,
    "Longitude": -77.297508
  },
  {
    "Country": "Japan",
    "Data_Year": 2018,
    "Happiness_Rank": 54,
    "Happiness_Score": 5.92,
    "Life_Expectancy": 84.4,
    "Population": 127000000,
    "Latitude": 36.204824,
    "Longitude": 138.252924
  },
  {
    "Country": "Japan",
    "Data_Year": 2017,
    "Happiness_Rank": 51,
    "Happiness_Score": 5.92,
    "Life_Expectancy": 84.2,
    "Population": 128000000,
    "Latitude": 36.204824,
    "Longitude": 138.252924
  },
  {
    "Country": "Serbia",
    "Data_Year": 2019,
    "Happiness_Rank": 78,
    "Happiness_Score": 5.4,
    "Life_Expectancy": 76,
    "Population": 8770000,
    "Latitude": 44.016521,
    "Longitude": 21.005859
  },
  {
    "Country": "Japan",
    "Data_Year": 2016,
    "Happiness_Rank": 53,
    "Happiness_Score": 5.92,
    "Life_Expectancy": 84.2,
    "Population": 128000000,
    "Latitude": 36.204824,
    "Longitude": 138.252924
  },
  {
    "Country": "Japan",
    "Data_Year": 2015,
    "Happiness_Rank": 46,
    "Happiness_Score": 5.99,
    "Life_Expectancy": 84.1,
    "Population": 128000000,
    "Latitude": 36.204824,
    "Longitude": 138.252924
  },
  {
    "Country": "Jordan",
    "Data_Year": 2015,
    "Happiness_Rank": 82,
    "Happiness_Score": 5.19,
    "Life_Expectancy": 79.1,
    "Population": 9270000,
    "Latitude": 30.585164,
    "Longitude": 36.238414
  },
  {
    "Country": "Jordan",
    "Data_Year": 2016,
    "Happiness_Rank": 80,
    "Happiness_Score": 5.3,
    "Life_Expectancy": 79.2,
    "Population": 9550000,
    "Latitude": 30.585164,
    "Longitude": 36.238414
  },
  {
    "Country": "Jordan",
    "Data_Year": 2018,
    "Happiness_Rank": 90,
    "Happiness_Score": 5.16,
    "Life_Expectancy": 79.5,
    "Population": 9970000,
    "Latitude": 30.585164,
    "Longitude": 36.238414
  },
  {
    "Country": "Brazil",
    "Data_Year": 2019,
    "Happiness_Rank": 28,
    "Happiness_Score": 6.42,
    "Life_Expectancy": 75.9,
    "Population": 211000000,
    "Latitude": -14.235004,
    "Longitude": -51.92528
  },
  {
    "Country": "Jordan",
    "Data_Year": 2017,
    "Happiness_Rank": 74,
    "Happiness_Score": 5.34,
    "Life_Expectancy": 79.3,
    "Population": 9790000,
    "Latitude": 30.585164,
    "Longitude": 36.238414
  },
  {
    "Country": "Kazakhstan",
    "Data_Year": 2018,
    "Happiness_Rank": 60,
    "Happiness_Score": 5.79,
    "Life_Expectancy": 72.5,
    "Population": 18300000,
    "Latitude": 48.019573,
    "Longitude": 66.923684
  },
  {
    "Country": "Kazakhstan",
    "Data_Year": 2017,
    "Happiness_Rank": 60,
    "Happiness_Score": 5.82,
    "Life_Expectancy": 72,
    "Population": 18100000,
    "Latitude": 48.019573,
    "Longitude": 66.923684
  },
  {
    "Country": "Kazakhstan",
    "Data_Year": 2015,
    "Happiness_Rank": 54,
    "Happiness_Score": 5.86,
    "Life_Expectancy": 71.7,
    "Population": 17600000,
    "Latitude": 48.019573,
    "Longitude": 66.923684
  },
  {
    "Country": "Kazakhstan",
    "Data_Year": 2016,
    "Happiness_Rank": 54,
    "Happiness_Score": 5.92,
    "Life_Expectancy": 71.8,
    "Population": 17800000,
    "Latitude": 48.019573,
    "Longitude": 66.923684
  },
  {
    "Country": "Armenia",
    "Data_Year": 2019,
    "Happiness_Rank": 129,
    "Happiness_Score": 4.32,
    "Life_Expectancy": 75.9,
    "Population": 2960000,
    "Latitude": 40.069099,
    "Longitude": 45.038189
  },
  {
    "Country": "Kenya",
    "Data_Year": 2015,
    "Happiness_Rank": 125,
    "Happiness_Score": 4.42,
    "Life_Expectancy": 64.7,
    "Population": 47900000,
    "Latitude": -0.023559,
    "Longitude": 37.906193
  },
  {
    "Country": "Kenya",
    "Data_Year": 2018,
    "Happiness_Rank": 124,
    "Happiness_Score": 4.41,
    "Life_Expectancy": 66.3,
    "Population": 51400000,
    "Latitude": -0.023559,
    "Longitude": 37.906193
  },
  {
    "Country": "Kenya",
    "Data_Year": 2017,
    "Happiness_Rank": 112,
    "Happiness_Score": 4.55,
    "Life_Expectancy": 65.9,
    "Population": 50200000,
    "Latitude": -0.023559,
    "Longitude": 37.906193
  },
  {
    "Country": "Kenya",
    "Data_Year": 2016,
    "Happiness_Rank": 122,
    "Happiness_Score": 4.36,
    "Life_Expectancy": 65.3,
    "Population": 49100000,
    "Latitude": -0.023559,
    "Longitude": 37.906193
  },
  {
    "Country": "Mexico",
    "Data_Year": 2019,
    "Happiness_Rank": 24,
    "Happiness_Score": 6.49,
    "Life_Expectancy": 75.6,
    "Population": 128000000,
    "Latitude": 23.634501,
    "Longitude": -102.552784
  },
  {
    "Country": "Kosovo",
    "Data_Year": 2017,
    "Happiness_Rank": 78,
    "Happiness_Score": 5.28,
    "Life_Expectancy": 74.2,
    "Population": 1807111,
    "Latitude": 42.602636,
    "Longitude": 20.902977
  },
  {
    "Country": "Kosovo",
    "Data_Year": 2015,
    "Happiness_Rank": 69,
    "Happiness_Score": 5.59,
    "Life_Expectancy": 73.6,
    "Population": 1804944,
    "Latitude": 42.602636,
    "Longitude": 20.902977
  },
  {
    "Country": "Lithuania",
    "Data_Year": 2019,
    "Happiness_Rank": 50,
    "Happiness_Score": 5.95,
    "Life_Expectancy": 75.4,
    "Population": 2760000,
    "Latitude": 55.169438,
    "Longitude": 23.881275
  },
  {
    "Country": "Kosovo",
    "Data_Year": 2018,
    "Happiness_Rank": 66,
    "Happiness_Score": 5.66,
    "Life_Expectancy": 74.7,
    "Population": 1808195,
    "Latitude": 42.602636,
    "Longitude": 20.902977
  },
  {
    "Country": "Kosovo",
    "Data_Year": 2016,
    "Happiness_Rank": 77,
    "Happiness_Score": 5.4,
    "Life_Expectancy": 73.9,
    "Population": 1806027,
    "Latitude": 42.602636,
    "Longitude": 20.902977
  },
  {
    "Country": "Kuwait",
    "Data_Year": 2016,
    "Happiness_Rank": 41,
    "Happiness_Score": 6.24,
    "Life_Expectancy": 83.1,
    "Population": 3960000,
    "Latitude": 29.31166,
    "Longitude": 47.481766
  },
  {
    "Country": "Kuwait",
    "Data_Year": 2018,
    "Happiness_Rank": 45,
    "Happiness_Score": 6.08,
    "Life_Expectancy": 83.2,
    "Population": 4140000,
    "Latitude": 29.31166,
    "Longitude": 47.481766
  },
  {
    "Country": "Romania",
    "Data_Year": 2019,
    "Happiness_Rank": 52,
    "Happiness_Score": 5.94,
    "Life_Expectancy": 75.4,
    "Population": 19400000,
    "Latitude": 45.943161,
    "Longitude": 24.96676
  },
  {
    "Country": "Kuwait",
    "Data_Year": 2017,
    "Happiness_Rank": 39,
    "Happiness_Score": 6.11,
    "Life_Expectancy": 83.1,
    "Population": 4060000,
    "Latitude": 29.31166,
    "Longitude": 47.481766
  },
  {
    "Country": "Kuwait",
    "Data_Year": 2015,
    "Happiness_Rank": 39,
    "Happiness_Score": 6.3,
    "Life_Expectancy": 82.9,
    "Population": 3840000,
    "Latitude": 29.31166,
    "Longitude": 47.481766
  },
  {
    "Country": "Kyrgyzstan",
    "Data_Year": 2015,
    "Happiness_Rank": 77,
    "Happiness_Score": 5.29,
    "Life_Expectancy": 70.88,
    "Population": 5959121,
    "Latitude": 41.20438,
    "Longitude": 74.766098
  },
  {
    "Country": "Latvia",
    "Data_Year": 2019,
    "Happiness_Rank": 53,
    "Happiness_Score": 5.93,
    "Life_Expectancy": 75.4,
    "Population": 1910000,
    "Latitude": 56.879635,
    "Longitude": 24.603189
  },
  {
    "Country": "Kyrgyzstan",
    "Data_Year": 2016,
    "Happiness_Rank": 85,
    "Happiness_Score": 5.18,
    "Life_Expectancy": 71.05,
    "Population": 6074330,
    "Latitude": 41.20438,
    "Longitude": 74.766098
  },
  {
    "Country": "Kyrgyzstan",
    "Data_Year": 2018,
    "Happiness_Rank": 92,
    "Happiness_Score": 5.13,
    "Life_Expectancy": 71.32,
    "Population": 6304030,
    "Latitude": 41.20438,
    "Longitude": 74.766098
  },
  {
    "Country": "Kyrgyzstan",
    "Data_Year": 2017,
    "Happiness_Rank": 98,
    "Happiness_Score": 5,
    "Life_Expectancy": 71.19,
    "Population": 6189733,
    "Latitude": 41.20438,
    "Longitude": 74.766098
  },
  {
    "Country": "Laos",
    "Data_Year": 2018,
    "Happiness_Rank": 110,
    "Happiness_Score": 4.62,
    "Life_Expectancy": 67.28,
    "Population": 7061507,
    "Latitude": 19.85627,
    "Longitude": 102.495496
  },
  {
    "Country": "Bulgaria",
    "Data_Year": 2019,
    "Happiness_Rank": 100,
    "Happiness_Score": 4.93,
    "Life_Expectancy": 75.1,
    "Population": 7000000,
    "Latitude": 42.733883,
    "Longitude": 25.48583
  },
  {
    "Country": "Laos",
    "Data_Year": 2016,
    "Happiness_Rank": 102,
    "Happiness_Score": 4.88,
    "Life_Expectancy": 66.92,
    "Population": 6845846,
    "Latitude": 19.85627,
    "Longitude": 102.495496
  },
  {
    "Country": "Laos",
    "Data_Year": 2015,
    "Happiness_Rank": 99,
    "Happiness_Score": 4.88,
    "Life_Expectancy": 66.55,
    "Population": 6741164,
    "Latitude": 19.85627,
    "Longitude": 102.495496
  },
  {
    "Country": "Latvia",
    "Data_Year": 2015,
    "Happiness_Rank": 89,
    "Happiness_Score": 5.1,
    "Life_Expectancy": 74.9,
    "Population": 2000000,
    "Latitude": 56.879635,
    "Longitude": 24.603189
  },
  {
    "Country": "Latvia",
    "Data_Year": 2018,
    "Happiness_Rank": 53,
    "Happiness_Score": 5.93,
    "Life_Expectancy": 75.3,
    "Population": 1930000,
    "Latitude": 56.879635,
    "Longitude": 24.603189
  },
  {
    "Country": "Venezuela",
    "Data_Year": 2019,
    "Happiness_Rank": 102,
    "Happiness_Score": 4.81,
    "Life_Expectancy": 75.1,
    "Population": 28500000,
    "Latitude": 6.42375,
    "Longitude": -66.58973
  },
  {
    "Country": "Latvia",
    "Data_Year": 2016,
    "Happiness_Rank": 68,
    "Happiness_Score": 5.56,
    "Life_Expectancy": 75,
    "Population": 1970000,
    "Latitude": 56.879635,
    "Longitude": 24.603189
  },
  {
    "Country": "Latvia",
    "Data_Year": 2017,
    "Happiness_Rank": 54,
    "Happiness_Score": 5.85,
    "Life_Expectancy": 75.2,
    "Population": 1950000,
    "Latitude": 56.879635,
    "Longitude": 24.603189
  },
  {
    "Country": "Lebanon",
    "Data_Year": 2016,
    "Happiness_Rank": 93,
    "Happiness_Score": 5.13,
    "Life_Expectancy": 78,
    "Population": 6710000,
    "Latitude": 33.854721,
    "Longitude": 35.862285
  },
  {
    "Country": "Lebanon",
    "Data_Year": 2017,
    "Happiness_Rank": 88,
    "Happiness_Score": 5.22,
    "Life_Expectancy": 78,
    "Population": 6820000,
    "Latitude": 33.854721,
    "Longitude": 35.862285
  },
  {
    "Country": "Lebanon",
    "Data_Year": 2018,
    "Happiness_Rank": 80,
    "Happiness_Score": 5.36,
    "Life_Expectancy": 78,
    "Population": 6860000,
    "Latitude": 33.854721,
    "Longitude": 35.862285
  },
  {
    "Country": "Lebanon",
    "Data_Year": 2015,
    "Happiness_Rank": 103,
    "Happiness_Score": 4.84,
    "Life_Expectancy": 77.8,
    "Population": 6530000,
    "Latitude": 33.854721,
    "Longitude": 35.862285
  },
  {
    "Country": "Malaysia",
    "Data_Year": 2019,
    "Happiness_Rank": 35,
    "Happiness_Score": 6.32,
    "Life_Expectancy": 75,
    "Population": 31900000,
    "Latitude": 4.210484,
    "Longitude": 101.975766
  },
  {
    "Country": "Lesotho",
    "Data_Year": 2015,
    "Happiness_Rank": 97,
    "Happiness_Score": 4.9,
    "Life_Expectancy": 50.5,
    "Population": 2060000,
    "Latitude": -29.609988,
    "Longitude": 28.233608
  },
  {
    "Country": "Lesotho",
    "Data_Year": 2018,
    "Happiness_Rank": 141,
    "Happiness_Score": 3.81,
    "Life_Expectancy": 55.5,
    "Population": 2110000,
    "Latitude": -29.609988,
    "Longitude": 28.233608
  },
  {
    "Country": "Mauritius",
    "Data_Year": 2019,
    "Happiness_Rank": 55,
    "Happiness_Score": 5.89,
    "Life_Expectancy": 75,
    "Population": 1270000,
    "Latitude": -20.348404,
    "Longitude": 57.552152
  },
  {
    "Country": "Lesotho",
    "Data_Year": 2017,
    "Happiness_Rank": 139,
    "Happiness_Score": 3.81,
    "Life_Expectancy": 54.7,
    "Population": 2090000,
    "Latitude": -29.609988,
    "Longitude": 28.233608
  },
  {
    "Country": "Liberia",
    "Data_Year": 2015,
    "Happiness_Rank": 116,
    "Happiness_Score": 4.57,
    "Life_Expectancy": 62,
    "Population": 4470000,
    "Latitude": 6.428055,
    "Longitude": -9.429499
  },
  {
    "Country": "Liberia",
    "Data_Year": 2016,
    "Happiness_Rank": 150,
    "Happiness_Score": 3.62,
    "Life_Expectancy": 63.9,
    "Population": 4590000,
    "Latitude": 6.428055,
    "Longitude": -9.429499
  },
  {
    "Country": "Liberia",
    "Data_Year": 2018,
    "Happiness_Rank": 149,
    "Happiness_Score": 3.5,
    "Life_Expectancy": 64.8,
    "Population": 4820000,
    "Latitude": 6.428055,
    "Longitude": -9.429499
  },
  {
    "Country": "Jamaica",
    "Data_Year": 2019,
    "Happiness_Rank": 56,
    "Happiness_Score": 5.89,
    "Life_Expectancy": 74.9,
    "Population": 2950000,
    "Latitude": 18.109581,
    "Longitude": -77.297508
  },
  {
    "Country": "Liberia",
    "Data_Year": 2017,
    "Happiness_Rank": 148,
    "Happiness_Score": 3.53,
    "Life_Expectancy": 64.4,
    "Population": 4700000,
    "Latitude": 6.428055,
    "Longitude": -9.429499
  },
  {
    "Country": "Libya",
    "Data_Year": 2016,
    "Happiness_Rank": 67,
    "Happiness_Score": 5.62,
    "Life_Expectancy": 72.4,
    "Population": 6490000,
    "Latitude": 26.3351,
    "Longitude": 17.228331
  },
  {
    "Country": "Libya",
    "Data_Year": 2018,
    "Happiness_Rank": 70,
    "Happiness_Score": 5.57,
    "Life_Expectancy": 73.2,
    "Population": 6680000,
    "Latitude": 26.3351,
    "Longitude": 17.228331
  },
  {
    "Country": "Libya",
    "Data_Year": 2015,
    "Happiness_Rank": 63,
    "Happiness_Score": 5.75,
    "Life_Expectancy": 73.1,
    "Population": 6420000,
    "Latitude": 26.3351,
    "Longitude": 17.228331
  },
  {
    "Country": "Libya",
    "Data_Year": 2017,
    "Happiness_Rank": 68,
    "Happiness_Score": 5.53,
    "Life_Expectancy": 73,
    "Population": 6580000,
    "Latitude": 26.3351,
    "Longitude": 17.228331
  },
  {
    "Country": "Vietnam",
    "Data_Year": 2019,
    "Happiness_Rank": 95,
    "Happiness_Score": 5.1,
    "Life_Expectancy": 74.7,
    "Population": 96500000,
    "Latitude": 14.058324,
    "Longitude": 108.277199
  },
  {
    "Country": "Lithuania",
    "Data_Year": 2017,
    "Happiness_Rank": 52,
    "Happiness_Score": 5.9,
    "Life_Expectancy": 75,
    "Population": 2850000,
    "Latitude": 55.169438,
    "Longitude": 23.881275
  },
  {
    "Country": "Lithuania",
    "Data_Year": 2016,
    "Happiness_Rank": 60,
    "Happiness_Score": 5.81,
    "Life_Expectancy": 74.9,
    "Population": 2890000,
    "Latitude": 55.169438,
    "Longitude": 23.881275
  },
  {
    "Country": "Lithuania",
    "Data_Year": 2015,
    "Happiness_Rank": 56,
    "Happiness_Score": 5.83,
    "Life_Expectancy": 74.7,
    "Population": 2930000,
    "Latitude": 55.169438,
    "Longitude": 23.881275
  },
  {
    "Country": "Lithuania",
    "Data_Year": 2018,
    "Happiness_Rank": 50,
    "Happiness_Score": 5.95,
    "Life_Expectancy": 75.3,
    "Population": 2800000,
    "Latitude": 55.169438,
    "Longitude": 23.881275
  },
  {
    "Country": "Bhutan",
    "Data_Year": 2019,
    "Happiness_Rank": 97,
    "Happiness_Score": 5.08,
    "Life_Expectancy": 74.7,
    "Population": 763000,
    "Latitude": 27.514162,
    "Longitude": 90.433601
  },
  {
    "Country": "Luxembourg",
    "Data_Year": 2015,
    "Happiness_Rank": 17,
    "Happiness_Score": 6.95,
    "Life_Expectancy": 81.4,
    "Population": 567000,
    "Latitude": 49.815273,
    "Longitude": 6.129583
  },
  {
    "Country": "Luxembourg",
    "Data_Year": 2017,
    "Happiness_Rank": 18,
    "Happiness_Score": 6.86,
    "Life_Expectancy": 81.7,
    "Population": 592000,
    "Latitude": 49.815273,
    "Longitude": 6.129583
  },
  {
    "Country": "Kosovo",
    "Data_Year": 2019,
    "Happiness_Rank": 66,
    "Happiness_Score": 5.66,
    "Life_Expectancy": 74.6,
    "Population": 1809280,
    "Latitude": 42.602636,
    "Longitude": 20.902977
  },
  {
    "Country": "Luxembourg",
    "Data_Year": 2016,
    "Happiness_Rank": 20,
    "Happiness_Score": 6.87,
    "Life_Expectancy": 81.6,
    "Population": 579000,
    "Latitude": 49.815273,
    "Longitude": 6.129583
  },
  {
    "Country": "Luxembourg",
    "Data_Year": 2018,
    "Happiness_Rank": 17,
    "Happiness_Score": 6.91,
    "Life_Expectancy": 81.8,
    "Population": 604000,
    "Latitude": 49.815273,
    "Longitude": 6.129583
  },
  {
    "Country": "Macedonia",
    "Data_Year": 2017,
    "Happiness_Rank": 92,
    "Happiness_Score": 5.18,
    "Life_Expectancy": 76,
    "Population": 2081996,
    "Latitude": 41.6086,
    "Longitude": 21.7453
  },
  {
    "Country": "Macedonia",
    "Data_Year": 2015,
    "Happiness_Rank": 93,
    "Happiness_Score": 5.01,
    "Life_Expectancy": 75.5,
    "Population": 2079328,
    "Latitude": 41.6086,
    "Longitude": 21.7453
  },
  {
    "Country": "Macedonia",
    "Data_Year": 2018,
    "Happiness_Rank": 89,
    "Happiness_Score": 5.18,
    "Life_Expectancy": 76.7,
    "Population": 2082957,
    "Latitude": 41.6086,
    "Longitude": 21.7453
  },
  {
    "Country": "Trinidad and Tobago",
    "Data_Year": 2019,
    "Happiness_Rank": 38,
    "Happiness_Score": 6.19,
    "Life_Expectancy": 74.5,
    "Population": 1390000,
    "Latitude": 10.6918,
    "Longitude": -61.2225
  },
  {
    "Country": "Macedonia",
    "Data_Year": 2016,
    "Happiness_Rank": 95,
    "Happiness_Score": 5.12,
    "Life_Expectancy": 75.4,
    "Population": 2080743,
    "Latitude": 41.6086,
    "Longitude": 21.7453
  },
  {
    "Country": "Madagascar",
    "Data_Year": 2015,
    "Happiness_Rank": 147,
    "Happiness_Score": 3.68,
    "Life_Expectancy": 63,
    "Population": 24200000,
    "Latitude": -18.766947,
    "Longitude": 46.869107
  },
  {
    "Country": "Madagascar",
    "Data_Year": 2017,
    "Happiness_Rank": 144,
    "Happiness_Score": 3.64,
    "Life_Expectancy": 63.5,
    "Population": 25600000,
    "Latitude": -18.766947,
    "Longitude": 46.869107
  },
  {
    "Country": "Madagascar",
    "Data_Year": 2016,
    "Happiness_Rank": 148,
    "Happiness_Score": 3.7,
    "Life_Expectancy": 63.2,
    "Population": 24900000,
    "Latitude": -18.766947,
    "Longitude": 46.869107
  },
  {
    "Country": "El Salvador",
    "Data_Year": 2019,
    "Happiness_Rank": 40,
    "Happiness_Score": 6.17,
    "Life_Expectancy": 74.5,
    "Population": 6450000,
    "Latitude": 13.7942,
    "Longitude": -88.8965
  },
  {
    "Country": "Madagascar",
    "Data_Year": 2018,
    "Happiness_Rank": 143,
    "Happiness_Score": 3.77,
    "Life_Expectancy": 63.9,
    "Population": 26300000,
    "Latitude": -18.766947,
    "Longitude": 46.869107
  },
  {
    "Country": "Malawi",
    "Data_Year": 2018,
    "Happiness_Rank": 147,
    "Happiness_Score": 3.59,
    "Life_Expectancy": 63.7,
    "Population": 18100000,
    "Latitude": -13.254308,
    "Longitude": 34.301525
  },
  {
    "Country": "Malawi",
    "Data_Year": 2015,
    "Happiness_Rank": 131,
    "Happiness_Score": 4.29,
    "Life_Expectancy": 61.7,
    "Population": 16700000,
    "Latitude": -13.254308,
    "Longitude": 34.301525
  },
  {
    "Country": "Malawi",
    "Data_Year": 2016,
    "Happiness_Rank": 132,
    "Happiness_Score": 4.16,
    "Life_Expectancy": 62.4,
    "Population": 17200000,
    "Latitude": -13.254308,
    "Longitude": 34.301525
  },
  {
    "Country": "Malawi",
    "Data_Year": 2017,
    "Happiness_Rank": 136,
    "Happiness_Score": 3.97,
    "Life_Expectancy": 63.2,
    "Population": 17700000,
    "Latitude": -13.254308,
    "Longitude": 34.301525
  },
  {
    "Country": "Belarus",
    "Data_Year": 2019,
    "Happiness_Rank": 73,
    "Happiness_Score": 5.48,
    "Life_Expectancy": 74.5,
    "Population": 9450000,
    "Latitude": 53.709807,
    "Longitude": 27.953389
  },
  {
    "Country": "Belize",
    "Data_Year": 2019,
    "Happiness_Rank": 49,
    "Happiness_Score": 5.96,
    "Life_Expectancy": 74.4,
    "Population": 390000,
    "Latitude": 17.189877,
    "Longitude": -88.49765
  },
  {
    "Country": "Malaysia",
    "Data_Year": 2016,
    "Happiness_Rank": 47,
    "Happiness_Score": 6,
    "Life_Expectancy": 74.7,
    "Population": 30700000,
    "Latitude": 4.210484,
    "Longitude": 101.975766
  },
  {
    "Country": "Malaysia",
    "Data_Year": 2015,
    "Happiness_Rank": 61,
    "Happiness_Score": 5.77,
    "Life_Expectancy": 74.6,
    "Population": 30300000,
    "Latitude": 4.210484,
    "Longitude": 101.975766
  },
  {
    "Country": "Malaysia",
    "Data_Year": 2017,
    "Happiness_Rank": 42,
    "Happiness_Score": 6.08,
    "Life_Expectancy": 74.7,
    "Population": 31100000,
    "Latitude": 4.210484,
    "Longitude": 101.975766
  },
  {
    "Country": "Malaysia",
    "Data_Year": 2018,
    "Happiness_Rank": 35,
    "Happiness_Score": 6.32,
    "Life_Expectancy": 74.9,
    "Population": 31500000,
    "Latitude": 4.210484,
    "Longitude": 101.975766
  },
  {
    "Country": "Mali",
    "Data_Year": 2018,
    "Happiness_Rank": 118,
    "Happiness_Score": 4.45,
    "Life_Expectancy": 62.4,
    "Population": 19100000,
    "Latitude": 17.570692,
    "Longitude": -3.996166
  },
  {
    "Country": "Morocco",
    "Data_Year": 2019,
    "Happiness_Rank": 85,
    "Happiness_Score": 5.25,
    "Life_Expectancy": 74.4,
    "Population": 36500000,
    "Latitude": 31.791702,
    "Longitude": -7.09262
  },
  {
    "Country": "Mali",
    "Data_Year": 2016,
    "Happiness_Rank": 135,
    "Happiness_Score": 4.07,
    "Life_Expectancy": 61.6,
    "Population": 18000000,
    "Latitude": 17.570692,
    "Longitude": -3.996166
  },
  {
    "Country": "Mali",
    "Data_Year": 2015,
    "Happiness_Rank": 138,
    "Happiness_Score": 4,
    "Life_Expectancy": 61.1,
    "Population": 17400000,
    "Latitude": 17.570692,
    "Longitude": -3.996166
  },
  {
    "Country": "Mali",
    "Data_Year": 2017,
    "Happiness_Rank": 127,
    "Happiness_Score": 4.19,
    "Life_Expectancy": 62,
    "Population": 18500000,
    "Latitude": 17.570692,
    "Longitude": -3.996166
  },
  {
    "Country": "Honduras",
    "Data_Year": 2019,
    "Happiness_Rank": 72,
    "Happiness_Score": 5.5,
    "Life_Expectancy": 74.3,
    "Population": 9750000,
    "Latitude": 15.199999,
    "Longitude": -86.241905
  },
  {
    "Country": "Malta",
    "Data_Year": 2017,
    "Happiness_Rank": 27,
    "Happiness_Score": 6.53,
    "Life_Expectancy": 81,
    "Population": 438000,
    "Latitude": 35.937496,
    "Longitude": 14.375416
  },
  {
    "Country": "Malta",
    "Data_Year": 2016,
    "Happiness_Rank": 30,
    "Happiness_Score": 6.49,
    "Life_Expectancy": 81,
    "Population": 436000,
    "Latitude": 35.937496,
    "Longitude": 14.375416
  },
  {
    "Country": "Malta",
    "Data_Year": 2018,
    "Happiness_Rank": 22,
    "Happiness_Score": 6.63,
    "Life_Expectancy": 81.1,
    "Population": 439000,
    "Latitude": 35.937496,
    "Longitude": 14.375416
  },
  {
    "Country": "Malta",
    "Data_Year": 2015,
    "Happiness_Rank": 37,
    "Happiness_Score": 6.3,
    "Life_Expectancy": 81.2,
    "Population": 434000,
    "Latitude": 35.937496,
    "Longitude": 14.375416
  },
  {
    "Country": "Mauritania",
    "Data_Year": 2017,
    "Happiness_Rank": 123,
    "Happiness_Score": 4.29,
    "Life_Expectancy": 70.5,
    "Population": 4280000,
    "Latitude": 21.00789,
    "Longitude": -10.940835
  },
  {
    "Country": "Mauritania",
    "Data_Year": 2018,
    "Happiness_Rank": 126,
    "Happiness_Score": 4.36,
    "Life_Expectancy": 70.8,
    "Population": 4400000,
    "Latitude": 21.00789,
    "Longitude": -10.940835
  },
  {
    "Country": "Mauritania",
    "Data_Year": 2016,
    "Happiness_Rank": 130,
    "Happiness_Score": 4.2,
    "Life_Expectancy": 70.2,
    "Population": 4160000,
    "Latitude": 21.00789,
    "Longitude": -10.940835
  },
  {
    "Country": "Bangladesh",
    "Data_Year": 2019,
    "Happiness_Rank": 115,
    "Happiness_Score": 4.5,
    "Life_Expectancy": 73.7,
    "Population": 163000000,
    "Latitude": 23.684994,
    "Longitude": 90.356331
  },
  {
    "Country": "Mauritania",
    "Data_Year": 2015,
    "Happiness_Rank": 124,
    "Happiness_Score": 4.44,
    "Life_Expectancy": 69.9,
    "Population": 4050000,
    "Latitude": 21.00789,
    "Longitude": -10.940835
  },
  {
    "Country": "Mauritius",
    "Data_Year": 2016,
    "Happiness_Rank": 66,
    "Happiness_Score": 5.65,
    "Life_Expectancy": 74.5,
    "Population": 1260000,
    "Latitude": -20.348404,
    "Longitude": 57.552152
  },
  {
    "Country": "United Arab Emirates",
    "Data_Year": 2019,
    "Happiness_Rank": 20,
    "Happiness_Score": 6.77,
    "Life_Expectancy": 73.6,
    "Population": 9770000,
    "Latitude": 23.4241,
    "Longitude": 53.8478
  },
  {
    "Country": "Mauritius",
    "Data_Year": 2015,
    "Happiness_Rank": 71,
    "Happiness_Score": 5.48,
    "Life_Expectancy": 74.5,
    "Population": 1260000,
    "Latitude": -20.348404,
    "Longitude": 57.552152
  },
  {
    "Country": "Mauritius",
    "Data_Year": 2017,
    "Happiness_Rank": 64,
    "Happiness_Score": 5.63,
    "Life_Expectancy": 74.8,
    "Population": 1260000,
    "Latitude": -20.348404,
    "Longitude": 57.552152
  },
  {
    "Country": "Mauritius",
    "Data_Year": 2018,
    "Happiness_Rank": 55,
    "Happiness_Score": 5.89,
    "Life_Expectancy": 74.9,
    "Population": 1270000,
    "Latitude": -20.348404,
    "Longitude": 57.552152
  },
  {
    "Country": "Mexico",
    "Data_Year": 2017,
    "Happiness_Rank": 25,
    "Happiness_Score": 6.58,
    "Life_Expectancy": 75.5,
    "Population": 125000000,
    "Latitude": 23.634501,
    "Longitude": -102.552784
  },
  {
    "Country": "Mexico",
    "Data_Year": 2018,
    "Happiness_Rank": 24,
    "Happiness_Score": 6.49,
    "Life_Expectancy": 75.6,
    "Population": 126000000,
    "Latitude": 23.634501,
    "Longitude": -102.552784
  },
  {
    "Country": "Dominican Republic",
    "Data_Year": 2019,
    "Happiness_Rank": 83,
    "Happiness_Score": 5.3,
    "Life_Expectancy": 73.5,
    "Population": 10700000,
    "Latitude": 18.7357,
    "Longitude": -70.1627
  },
  {
    "Country": "Mexico",
    "Data_Year": 2015,
    "Happiness_Rank": 14,
    "Happiness_Score": 7.19,
    "Life_Expectancy": 75.9,
    "Population": 122000000,
    "Latitude": 23.634501,
    "Longitude": -102.552784
  },
  {
    "Country": "Mexico",
    "Data_Year": 2016,
    "Happiness_Rank": 21,
    "Happiness_Score": 6.78,
    "Life_Expectancy": 75.9,
    "Population": 123000000,
    "Latitude": 23.634501,
    "Longitude": -102.552784
  },
  {
    "Country": "Moldova",
    "Data_Year": 2017,
    "Happiness_Rank": 56,
    "Happiness_Score": 5.84,
    "Life_Expectancy": 72.9,
    "Population": 4060000,
    "Latitude": 47.411631,
    "Longitude": 28.369885
  },
  {
    "Country": "Moldova",
    "Data_Year": 2015,
    "Happiness_Rank": 52,
    "Happiness_Score": 5.89,
    "Life_Expectancy": 71.8,
    "Population": 4070000,
    "Latitude": 47.411631,
    "Longitude": 28.369885
  },
  {
    "Country": "Moldova",
    "Data_Year": 2016,
    "Happiness_Rank": 55,
    "Happiness_Score": 5.9,
    "Life_Expectancy": 72.4,
    "Population": 4070000,
    "Latitude": 47.411631,
    "Longitude": 28.369885
  },
  {
    "Country": "Bolivia",
    "Data_Year": 2019,
    "Happiness_Rank": 62,
    "Happiness_Score": 5.75,
    "Life_Expectancy": 73.3,
    "Population": 11500000,
    "Latitude": -16.290154,
    "Longitude": -63.588653
  },
  {
    "Country": "Moldova",
    "Data_Year": 2018,
    "Happiness_Rank": 67,
    "Happiness_Score": 5.64,
    "Life_Expectancy": 73,
    "Population": 4050000,
    "Latitude": 47.411631,
    "Longitude": 28.369885
  },
  {
    "Country": "Mongolia",
    "Data_Year": 2016,
    "Happiness_Rank": 101,
    "Happiness_Score": 4.91,
    "Life_Expectancy": 68.8,
    "Population": 3060000,
    "Latitude": 46.862496,
    "Longitude": 103.846656
  },
  {
    "Country": "Mongolia",
    "Data_Year": 2017,
    "Happiness_Rank": 100,
    "Happiness_Score": 4.95,
    "Life_Expectancy": 68.9,
    "Population": 3110000,
    "Latitude": 46.862496,
    "Longitude": 103.846656
  },
  {
    "Country": "Libya",
    "Data_Year": 2019,
    "Happiness_Rank": 70,
    "Happiness_Score": 5.57,
    "Life_Expectancy": 73.3,
    "Population": 6780000,
    "Latitude": 26.3351,
    "Longitude": 17.228331
  },
  {
    "Country": "Mongolia",
    "Data_Year": 2018,
    "Happiness_Rank": 94,
    "Happiness_Score": 5.12,
    "Life_Expectancy": 69.1,
    "Population": 3170000,
    "Latitude": 46.862496,
    "Longitude": 103.846656
  },
  {
    "Country": "Mongolia",
    "Data_Year": 2015,
    "Happiness_Rank": 100,
    "Happiness_Score": 4.87,
    "Life_Expectancy": 68.6,
    "Population": 3000000,
    "Latitude": 46.862496,
    "Longitude": 103.846656
  },
  {
    "Country": "Georgia",
    "Data_Year": 2019,
    "Happiness_Rank": 128,
    "Happiness_Score": 4.34,
    "Life_Expectancy": 73.2,
    "Population": 4000000,
    "Latitude": 42.315407,
    "Longitude": 43.356892
  },
  {
    "Country": "Montenegro",
    "Data_Year": 2016,
    "Happiness_Rank": 88,
    "Happiness_Score": 5.16,
    "Life_Expectancy": 76.4,
    "Population": 627000,
    "Latitude": 42.708678,
    "Longitude": 19.37439
  },
  {
    "Country": "Montenegro",
    "Data_Year": 2017,
    "Happiness_Rank": 83,
    "Happiness_Score": 5.24,
    "Life_Expectancy": 76.5,
    "Population": 628000,
    "Latitude": 42.708678,
    "Longitude": 19.37439
  },
  {
    "Country": "Montenegro",
    "Data_Year": 2015,
    "Happiness_Rank": 82,
    "Happiness_Score": 5.19,
    "Life_Expectancy": 76.4,
    "Population": 627000,
    "Latitude": 42.708678,
    "Longitude": 19.37439
  },
  {
    "Country": "Montenegro",
    "Data_Year": 2018,
    "Happiness_Rank": 81,
    "Happiness_Score": 5.35,
    "Life_Expectancy": 76.6,
    "Population": 628000,
    "Latitude": 42.708678,
    "Longitude": 19.37439
  },
  {
    "Country": "Guatemala",
    "Data_Year": 2019,
    "Happiness_Rank": 30,
    "Happiness_Score": 6.38,
    "Life_Expectancy": 73.1,
    "Population": 17600000,
    "Latitude": 15.783471,
    "Longitude": -90.230759
  },
  {
    "Country": "Morocco",
    "Data_Year": 2016,
    "Happiness_Rank": 90,
    "Happiness_Score": 5.15,
    "Life_Expectancy": 73.7,
    "Population": 35100000,
    "Latitude": 31.791702,
    "Longitude": -7.09262
  },
  {
    "Country": "Morocco",
    "Data_Year": 2017,
    "Happiness_Rank": 84,
    "Happiness_Score": 5.24,
    "Life_Expectancy": 74,
    "Population": 35600000,
    "Latitude": 31.791702,
    "Longitude": -7.09262
  },
  {
    "Country": "Morocco",
    "Data_Year": 2018,
    "Happiness_Rank": 85,
    "Happiness_Score": 5.25,
    "Life_Expectancy": 74.2,
    "Population": 36000000,
    "Latitude": 31.791702,
    "Longitude": -7.09262
  },
  {
    "Country": "Morocco",
    "Data_Year": 2015,
    "Happiness_Rank": 92,
    "Happiness_Score": 5.01,
    "Life_Expectancy": 73.5,
    "Population": 34700000,
    "Latitude": 31.791702,
    "Longitude": -7.09262
  },
  {
    "Country": "Moldova",
    "Data_Year": 2019,
    "Happiness_Rank": 67,
    "Happiness_Score": 5.64,
    "Life_Expectancy": 73.1,
    "Population": 4040000,
    "Latitude": 47.411631,
    "Longitude": 28.369885
  },
  {
    "Country": "Mozambique",
    "Data_Year": 2017,
    "Happiness_Rank": 113,
    "Happiness_Score": 4.55,
    "Life_Expectancy": 58.4,
    "Population": 28600000,
    "Latitude": -18.665695,
    "Longitude": 35.529562
  },
  {
    "Country": "Mozambique",
    "Data_Year": 2015,
    "Happiness_Rank": 94,
    "Happiness_Score": 4.97,
    "Life_Expectancy": 56.2,
    "Population": 27000000,
    "Latitude": -18.665695,
    "Longitude": 35.529562
  },
  {
    "Country": "Mozambique",
    "Data_Year": 2018,
    "Happiness_Rank": 123,
    "Happiness_Score": 4.42,
    "Life_Expectancy": 59.2,
    "Population": 29500000,
    "Latitude": -18.665695,
    "Longitude": 35.529562
  },
  {
    "Country": "Myanmar",
    "Data_Year": 2016,
    "Happiness_Rank": 119,
    "Happiness_Score": 4.39,
    "Life_Expectancy": 68.3,
    "Population": 53000000,
    "Latitude": 21.9162,
    "Longitude": 95.956
  },
  {
    "Country": "Myanmar",
    "Data_Year": 2017,
    "Happiness_Rank": 114,
    "Happiness_Score": 4.55,
    "Life_Expectancy": 68.5,
    "Population": 53400000,
    "Latitude": 21.9162,
    "Longitude": 95.956
  },
  {
    "Country": "Kazakhstan",
    "Data_Year": 2019,
    "Happiness_Rank": 60,
    "Happiness_Score": 5.79,
    "Life_Expectancy": 72.8,
    "Population": 18600000,
    "Latitude": 48.019573,
    "Longitude": 66.923684
  },
  {
    "Country": "Myanmar",
    "Data_Year": 2018,
    "Happiness_Rank": 130,
    "Happiness_Score": 4.31,
    "Life_Expectancy": 68.8,
    "Population": 53700000,
    "Latitude": 21.9162,
    "Longitude": 95.956
  },
  {
    "Country": "Myanmar",
    "Data_Year": 2015,
    "Happiness_Rank": 129,
    "Happiness_Score": 4.31,
    "Life_Expectancy": 67.8,
    "Population": 52700000,
    "Latitude": 21.9162,
    "Longitude": 95.956
  },
  {
    "Country": "Russia",
    "Data_Year": 2019,
    "Happiness_Rank": 59,
    "Happiness_Score": 5.81,
    "Life_Expectancy": 72.5,
    "Population": 146000000,
    "Latitude": 61.52401,
    "Longitude": 105.318756
  },
  {
    "Country": "Namibia",
    "Data_Year": 2018,
    "Happiness_Rank": 119,
    "Happiness_Score": 4.44,
    "Life_Expectancy": 66.9,
    "Population": 2450000,
    "Latitude": -22.95764,
    "Longitude": 18.49041
  },
  {
    "Country": "Namibia",
    "Data_Year": 2016,
    "Happiness_Rank": 113,
    "Happiness_Score": 4.57,
    "Life_Expectancy": 66.2,
    "Population": 2360000,
    "Latitude": -22.95764,
    "Longitude": 18.49041
  },
  {
    "Country": "Namibia",
    "Data_Year": 2017,
    "Happiness_Rank": 111,
    "Happiness_Score": 4.57,
    "Life_Expectancy": 66.5,
    "Population": 2400000,
    "Latitude": -22.95764,
    "Longitude": 18.49041
  },
  {
    "Country": "Nepal",
    "Data_Year": 2017,
    "Happiness_Rank": 99,
    "Happiness_Score": 4.96,
    "Life_Expectancy": 70.9,
    "Population": 27600000,
    "Latitude": 28.394857,
    "Longitude": 84.124008
  },
  {
    "Country": "Nepal",
    "Data_Year": 2015,
    "Happiness_Rank": 121,
    "Happiness_Score": 4.51,
    "Life_Expectancy": 69.6,
    "Population": 27000000,
    "Latitude": 28.394857,
    "Longitude": 84.124008
  },
  {
    "Country": "Nepal",
    "Data_Year": 2016,
    "Happiness_Rank": 107,
    "Happiness_Score": 4.79,
    "Life_Expectancy": 70.6,
    "Population": 27300000,
    "Latitude": 28.394857,
    "Longitude": 84.124008
  },
  {
    "Country": "Indonesia",
    "Data_Year": 2019,
    "Happiness_Rank": 96,
    "Happiness_Score": 5.09,
    "Life_Expectancy": 71.9,
    "Population": 271000000,
    "Latitude": -0.789275,
    "Longitude": 113.921327
  },
  {
    "Country": "Nepal",
    "Data_Year": 2018,
    "Happiness_Rank": 101,
    "Happiness_Score": 4.88,
    "Life_Expectancy": 71.2,
    "Population": 28100000,
    "Latitude": 28.394857,
    "Longitude": 84.124008
  },
  {
    "Country": "Netherlands",
    "Data_Year": 2016,
    "Happiness_Rank": 7,
    "Happiness_Score": 7.34,
    "Life_Expectancy": 81.5,
    "Population": 17000000,
    "Latitude": 52.132633,
    "Longitude": 5.291266
  },
  {
    "Country": "Netherlands",
    "Data_Year": 2018,
    "Happiness_Rank": 6,
    "Happiness_Score": 7.44,
    "Life_Expectancy": 81.7,
    "Population": 17100000,
    "Latitude": 52.132633,
    "Longitude": 5.291266
  },
  {
    "Country": "Nepal",
    "Data_Year": 2019,
    "Happiness_Rank": 101,
    "Happiness_Score": 4.88,
    "Life_Expectancy": 71.5,
    "Population": 28600000,
    "Latitude": 28.394857,
    "Longitude": 84.124008
  },
  {
    "Country": "Netherlands",
    "Data_Year": 2015,
    "Happiness_Rank": 7,
    "Happiness_Score": 7.38,
    "Life_Expectancy": 81.5,
    "Population": 16900000,
    "Latitude": 52.132633,
    "Longitude": 5.291266
  },
  {
    "Country": "Netherlands",
    "Data_Year": 2017,
    "Happiness_Rank": 6,
    "Happiness_Score": 7.38,
    "Life_Expectancy": 81.5,
    "Population": 17000000,
    "Latitude": 52.132633,
    "Longitude": 5.291266
  },
  {
    "Country": "New Zealand",
    "Data_Year": 2018,
    "Happiness_Rank": 8,
    "Happiness_Score": 7.32,
    "Life_Expectancy": 81.8,
    "Population": 4740000,
    "Latitude": 40.9006,
    "Longitude": -174.886
  },
  {
    "Country": "New Zealand",
    "Data_Year": 2017,
    "Happiness_Rank": 8,
    "Happiness_Score": 7.31,
    "Life_Expectancy": 81.6,
    "Population": 4700000,
    "Latitude": 40.9006,
    "Longitude": -174.886
  },
  {
    "Country": "New Zealand",
    "Data_Year": 2015,
    "Happiness_Rank": 9,
    "Happiness_Score": 7.29,
    "Life_Expectancy": 81.5,
    "Population": 4610000,
    "Latitude": 40.9006,
    "Longitude": -174.886
  },
  {
    "Country": "New Zealand",
    "Data_Year": 2016,
    "Happiness_Rank": 8,
    "Happiness_Score": 7.33,
    "Life_Expectancy": 81.7,
    "Population": 4660000,
    "Latitude": 40.9006,
    "Longitude": -174.886
  },
  {
    "Country": "Syria",
    "Data_Year": 2019,
    "Happiness_Rank": 150,
    "Happiness_Score": 3.46,
    "Life_Expectancy": 71.5,
    "Population": 17100000,
    "Latitude": 34.802075,
    "Longitude": 38.996815
  },
  {
    "Country": "Kyrgyzstan",
    "Data_Year": 2019,
    "Happiness_Rank": 92,
    "Happiness_Score": 5.13,
    "Life_Expectancy": 71.45,
    "Population": 6415850,
    "Latitude": 41.20438,
    "Longitude": 74.766098
  },
  {
    "Country": "Nicaragua",
    "Data_Year": 2016,
    "Happiness_Rank": 48,
    "Happiness_Score": 5.99,
    "Life_Expectancy": 78.5,
    "Population": 6300000,
    "Latitude": 12.865416,
    "Longitude": -85.207229
  },
  {
    "Country": "Nicaragua",
    "Data_Year": 2017,
    "Happiness_Rank": 43,
    "Happiness_Score": 6.07,
    "Life_Expectancy": 78.8,
    "Population": 6380000,
    "Latitude": 12.865416,
    "Longitude": -85.207229
  },
  {
    "Country": "Nicaragua",
    "Data_Year": 2015,
    "Happiness_Rank": 57,
    "Happiness_Score": 5.83,
    "Life_Expectancy": 78.1,
    "Population": 6220000,
    "Latitude": 12.865416,
    "Longitude": -85.207229
  },
  {
    "Country": "Nicaragua",
    "Data_Year": 2018,
    "Happiness_Rank": 41,
    "Happiness_Score": 6.14,
    "Life_Expectancy": 79,
    "Population": 6470000,
    "Latitude": 12.865416,
    "Longitude": -85.207229
  },
  {
    "Country": "Niger",
    "Data_Year": 2015,
    "Happiness_Rank": 144,
    "Happiness_Score": 3.84,
    "Life_Expectancy": 61.3,
    "Population": 20000000,
    "Latitude": 17.607789,
    "Longitude": 8.081666
  },
  {
    "Country": "Niger",
    "Data_Year": 2016,
    "Happiness_Rank": 142,
    "Happiness_Score": 3.86,
    "Life_Expectancy": 61.9,
    "Population": 20800000,
    "Latitude": 17.607789,
    "Longitude": 8.081666
  },
  {
    "Country": "Niger",
    "Data_Year": 2018,
    "Happiness_Rank": 134,
    "Happiness_Score": 4.17,
    "Life_Expectancy": 62.8,
    "Population": 22400000,
    "Latitude": 17.607789,
    "Longitude": 8.081666
  },
  {
    "Country": "Azerbaijan",
    "Data_Year": 2019,
    "Happiness_Rank": 87,
    "Happiness_Score": 5.2,
    "Life_Expectancy": 71.1,
    "Population": 10000000,
    "Latitude": 40.143105,
    "Longitude": 47.576927
  },
  {
    "Country": "Niger",
    "Data_Year": 2017,
    "Happiness_Rank": 135,
    "Happiness_Score": 4.03,
    "Life_Expectancy": 62.4,
    "Population": 21600000,
    "Latitude": 17.607789,
    "Longitude": 8.081666
  },
  {
    "Country": "Nigeria",
    "Data_Year": 2016,
    "Happiness_Rank": 103,
    "Happiness_Score": 4.88,
    "Life_Expectancy": 63.9,
    "Population": 186000000,
    "Latitude": 9.081999,
    "Longitude": 8.675277
  },
  {
    "Country": "Nigeria",
    "Data_Year": 2015,
    "Happiness_Rank": 78,
    "Happiness_Score": 5.27,
    "Life_Expectancy": 63.4,
    "Population": 181000000,
    "Latitude": 9.081999,
    "Longitude": 8.675277
  },
  {
    "Country": "Nigeria",
    "Data_Year": 2017,
    "Happiness_Rank": 95,
    "Happiness_Score": 5.07,
    "Life_Expectancy": 64.3,
    "Population": 191000000,
    "Latitude": 9.081999,
    "Longitude": 8.675277
  },
  {
    "Country": "Nigeria",
    "Data_Year": 2018,
    "Happiness_Rank": 91,
    "Happiness_Score": 5.16,
    "Life_Expectancy": 64.8,
    "Population": 196000000,
    "Latitude": 9.081999,
    "Longitude": 8.675277
  },
  {
    "Country": "Egypt",
    "Data_Year": 2019,
    "Happiness_Rank": 122,
    "Happiness_Score": 4.42,
    "Life_Expectancy": 71,
    "Population": 100000000,
    "Latitude": 26.820553,
    "Longitude": 30.802498
  },
  {
    "Country": "North Cyprus",
    "Data_Year": 2016,
    "Happiness_Rank": 62,
    "Happiness_Score": 5.77,
    "Life_Expectancy": 80.35,
    "Population": 1170187,
    "Latitude": 35.248,
    "Longitude": 33.6577
  },
  {
    "Country": "North Cyprus",
    "Data_Year": 2015,
    "Happiness_Rank": 66,
    "Happiness_Score": 5.7,
    "Life_Expectancy": 80.18,
    "Population": 1160985,
    "Latitude": 35.248,
    "Longitude": 33.6577
  },
  {
    "Country": "North Cyprus",
    "Data_Year": 2017,
    "Happiness_Rank": 61,
    "Happiness_Score": 5.81,
    "Life_Expectancy": 80.51,
    "Population": 1179678,
    "Latitude": 35.248,
    "Longitude": 33.6577
  },
  {
    "Country": "Northern Cyprus",
    "Data_Year": 2018,
    "Happiness_Rank": 58,
    "Happiness_Score": 5.84,
    "Life_Expectancy": 80.67,
    "Population": 1189265,
    "Latitude": 35.248,
    "Longitude": 33.6577
  },
  {
    "Country": "Mauritania",
    "Data_Year": 2019,
    "Happiness_Rank": 126,
    "Happiness_Score": 4.36,
    "Life_Expectancy": 71,
    "Population": 4530000,
    "Latitude": 21.00789,
    "Longitude": -10.940835
  },
  {
    "Country": "Norway",
    "Data_Year": 2015,
    "Happiness_Rank": 4,
    "Happiness_Score": 7.52,
    "Life_Expectancy": 82.3,
    "Population": 5200000,
    "Latitude": 60.472024,
    "Longitude": 8.468946
  },
  {
    "Country": "Norway",
    "Data_Year": 2017,
    "Happiness_Rank": 1,
    "Happiness_Score": 7.54,
    "Life_Expectancy": 82.3,
    "Population": 5300000,
    "Latitude": 60.472024,
    "Longitude": 8.468946
  },
  {
    "Country": "Tajikistan",
    "Data_Year": 2019,
    "Happiness_Rank": 88,
    "Happiness_Score": 5.2,
    "Life_Expectancy": 70.8,
    "Population": 9320000,
    "Latitude": 38.861034,
    "Longitude": 71.276093
  },
  {
    "Country": "Norway",
    "Data_Year": 2016,
    "Happiness_Rank": 4,
    "Happiness_Score": 7.5,
    "Life_Expectancy": 82.4,
    "Population": 5250000,
    "Latitude": 60.472024,
    "Longitude": 8.468946
  },
  {
    "Country": "Norway",
    "Data_Year": 2018,
    "Happiness_Rank": 2,
    "Happiness_Score": 7.59,
    "Life_Expectancy": 82.5,
    "Population": 5340000,
    "Latitude": 60.472024,
    "Longitude": 8.468946
  },
  {
    "Country": "Oman",
    "Data_Year": 2015,
    "Happiness_Rank": 22,
    "Happiness_Score": 6.85,
    "Life_Expectancy": 76.4,
    "Population": 4270000,
    "Latitude": 21.512583,
    "Longitude": 55.923255
  },
  {
    "Country": "Pakistan",
    "Data_Year": 2017,
    "Happiness_Rank": 80,
    "Happiness_Score": 5.27,
    "Life_Expectancy": 66.8,
    "Population": 208000000,
    "Latitude": 30.375321,
    "Longitude": 69.345116
  },
  {
    "Country": "Pakistan",
    "Data_Year": 2018,
    "Happiness_Rank": 75,
    "Happiness_Score": 5.47,
    "Life_Expectancy": 67,
    "Population": 212000000,
    "Latitude": 30.375321,
    "Longitude": 69.345116
  },
  {
    "Country": "Sudan",
    "Data_Year": 2019,
    "Happiness_Rank": 137,
    "Happiness_Score": 4.14,
    "Life_Expectancy": 70.8,
    "Population": 42800000,
    "Latitude": 12.862807,
    "Longitude": 30.217636
  },
  {
    "Country": "Pakistan",
    "Data_Year": 2016,
    "Happiness_Rank": 92,
    "Happiness_Score": 5.13,
    "Life_Expectancy": 66.4,
    "Population": 204000000,
    "Latitude": 30.375321,
    "Longitude": 69.345116
  },
  {
    "Country": "Pakistan",
    "Data_Year": 2015,
    "Happiness_Rank": 81,
    "Happiness_Score": 5.19,
    "Life_Expectancy": 66,
    "Population": 199000000,
    "Latitude": 30.375321,
    "Longitude": 69.345116
  },
  {
    "Country": "Palestinian Territories",
    "Data_Year": 2017,
    "Happiness_Rank": 103,
    "Happiness_Score": 4.78,
    "Life_Expectancy": 76.8,
    "Population": 4750000,
    "Latitude": 31.9522,
    "Longitude": 35.2332
  },
  {
    "Country": "Palestinian Territories",
    "Data_Year": 2018,
    "Happiness_Rank": 104,
    "Happiness_Score": 4.74,
    "Life_Expectancy": 77,
    "Population": 4860000,
    "Latitude": 31.9522,
    "Longitude": 35.2332
  },
  {
    "Country": "Palestinian Territories",
    "Data_Year": 2016,
    "Happiness_Rank": 108,
    "Happiness_Score": 4.75,
    "Life_Expectancy": 76.6,
    "Population": 4640000,
    "Latitude": 31.9522,
    "Longitude": 35.2332
  },
  {
    "Country": "Ukraine",
    "Data_Year": 2019,
    "Happiness_Rank": 138,
    "Happiness_Score": 4.1,
    "Life_Expectancy": 70.8,
    "Population": 44000000,
    "Latitude": 48.379433,
    "Longitude": 31.16558
  },
  {
    "Country": "Palestinian Territories",
    "Data_Year": 2015,
    "Happiness_Rank": 108,
    "Happiness_Score": 4.72,
    "Life_Expectancy": 76.2,
    "Population": 4530000,
    "Latitude": 31.9522,
    "Longitude": 35.2332
  },
  {
    "Country": "Panama",
    "Data_Year": 2015,
    "Happiness_Rank": 25,
    "Happiness_Score": 6.79,
    "Life_Expectancy": 78.9,
    "Population": 3970000,
    "Latitude": 8.537981,
    "Longitude": -80.782127
  },
  {
    "Country": "Panama",
    "Data_Year": 2016,
    "Happiness_Rank": 25,
    "Happiness_Score": 6.7,
    "Life_Expectancy": 79.1,
    "Population": 4040000,
    "Latitude": 8.537981,
    "Longitude": -80.782127
  },
  {
    "Country": "Uzbekistan",
    "Data_Year": 2019,
    "Happiness_Rank": 44,
    "Happiness_Score": 6.1,
    "Life_Expectancy": 70.7,
    "Population": 33000000,
    "Latitude": 41.377491,
    "Longitude": 64.585262
  },
  {
    "Country": "Panama",
    "Data_Year": 2018,
    "Happiness_Rank": 27,
    "Happiness_Score": 6.43,
    "Life_Expectancy": 79.5,
    "Population": 4180000,
    "Latitude": 8.537981,
    "Longitude": -80.782127
  },
  {
    "Country": "Panama",
    "Data_Year": 2017,
    "Happiness_Rank": 30,
    "Happiness_Score": 6.45,
    "Life_Expectancy": 79.3,
    "Population": 4110000,
    "Latitude": 8.537981,
    "Longitude": -80.782127
  },
  {
    "Country": "Paraguay",
    "Data_Year": 2018,
    "Happiness_Rank": 64,
    "Happiness_Score": 5.68,
    "Life_Expectancy": 76.3,
    "Population": 6960000,
    "Latitude": -23.442503,
    "Longitude": -58.443832
  },
  {
    "Country": "Cambodia",
    "Data_Year": 2019,
    "Happiness_Rank": 120,
    "Happiness_Score": 4.43,
    "Life_Expectancy": 70.4,
    "Population": 16500000,
    "Latitude": 12.565679,
    "Longitude": 104.990963
  },
  {
    "Country": "Paraguay",
    "Data_Year": 2016,
    "Happiness_Rank": 70,
    "Happiness_Score": 5.54,
    "Life_Expectancy": 75.9,
    "Population": 6780000,
    "Latitude": -23.442503,
    "Longitude": -58.443832
  },
  {
    "Country": "Paraguay",
    "Data_Year": 2015,
    "Happiness_Rank": 53,
    "Happiness_Score": 5.88,
    "Life_Expectancy": 75.8,
    "Population": 6690000,
    "Latitude": -23.442503,
    "Longitude": -58.443832
  },
  {
    "Country": "Paraguay",
    "Data_Year": 2017,
    "Happiness_Rank": 70,
    "Happiness_Score": 5.49,
    "Life_Expectancy": 76.1,
    "Population": 6870000,
    "Latitude": -23.442503,
    "Longitude": -58.443832
  },
  {
    "Country": "Turkmenistan",
    "Data_Year": 2019,
    "Happiness_Rank": 68,
    "Happiness_Score": 5.64,
    "Life_Expectancy": 70.3,
    "Population": 5940000,
    "Latitude": 38.969719,
    "Longitude": 59.556278
  },
  {
    "Country": "Peru",
    "Data_Year": 2018,
    "Happiness_Rank": 65,
    "Happiness_Score": 5.66,
    "Life_Expectancy": 80.6,
    "Population": 32000000,
    "Latitude": -9.189967,
    "Longitude": -75.015152
  },
  {
    "Country": "Peru",
    "Data_Year": 2015,
    "Happiness_Rank": 58,
    "Happiness_Score": 5.82,
    "Life_Expectancy": 80,
    "Population": 30500000,
    "Latitude": -9.189967,
    "Longitude": -75.015152
  },
  {
    "Country": "Peru",
    "Data_Year": 2017,
    "Happiness_Rank": 63,
    "Happiness_Score": 5.72,
    "Life_Expectancy": 80.3,
    "Population": 31400000,
    "Latitude": -9.189967,
    "Longitude": -75.015152
  },
  {
    "Country": "Peru",
    "Data_Year": 2016,
    "Happiness_Rank": 64,
    "Happiness_Score": 5.74,
    "Life_Expectancy": 80.2,
    "Population": 30900000,
    "Latitude": -9.189967,
    "Longitude": -75.015152
  },
  {
    "Country": "Philippines",
    "Data_Year": 2019,
    "Happiness_Rank": 71,
    "Happiness_Score": 5.52,
    "Life_Expectancy": 70,
    "Population": 108000000,
    "Latitude": 12.879721,
    "Longitude": 121.774017
  },
  {
    "Country": "Philippines",
    "Data_Year": 2015,
    "Happiness_Rank": 90,
    "Happiness_Score": 5.07,
    "Life_Expectancy": 69.2,
    "Population": 102000000,
    "Latitude": 12.879721,
    "Longitude": 121.774017
  },
  {
    "Country": "Philippines",
    "Data_Year": 2016,
    "Happiness_Rank": 82,
    "Happiness_Score": 5.28,
    "Life_Expectancy": 69.5,
    "Population": 104000000,
    "Latitude": 12.879721,
    "Longitude": 121.774017
  },
  {
    "Country": "Philippines",
    "Data_Year": 2017,
    "Happiness_Rank": 72,
    "Happiness_Score": 5.43,
    "Life_Expectancy": 69.7,
    "Population": 105000000,
    "Latitude": 12.879721,
    "Longitude": 121.774017
  },
  {
    "Country": "Philippines",
    "Data_Year": 2018,
    "Happiness_Rank": 71,
    "Happiness_Score": 5.52,
    "Life_Expectancy": 69.9,
    "Population": 107000000,
    "Latitude": 12.879721,
    "Longitude": 121.774017
  },
  {
    "Country": "Poland",
    "Data_Year": 2016,
    "Happiness_Rank": 57,
    "Happiness_Score": 5.84,
    "Life_Expectancy": 77.8,
    "Population": 38000000,
    "Latitude": 51.919438,
    "Longitude": 19.145136
  },
  {
    "Country": "Poland",
    "Data_Year": 2018,
    "Happiness_Rank": 42,
    "Happiness_Score": 6.12,
    "Life_Expectancy": 78.2,
    "Population": 37900000,
    "Latitude": 51.919438,
    "Longitude": 19.145136
  },
  {
    "Country": "Poland",
    "Data_Year": 2015,
    "Happiness_Rank": 60,
    "Happiness_Score": 5.79,
    "Life_Expectancy": 77.5,
    "Population": 38000000,
    "Latitude": 51.919438,
    "Longitude": 19.145136
  },
  {
    "Country": "Poland",
    "Data_Year": 2017,
    "Happiness_Rank": 46,
    "Happiness_Score": 5.97,
    "Life_Expectancy": 78,
    "Population": 38000000,
    "Latitude": 51.919438,
    "Longitude": 19.145136
  },
  {
    "Country": "Botswana",
    "Data_Year": 2019,
    "Happiness_Rank": 146,
    "Happiness_Score": 3.59,
    "Life_Expectancy": 69.8,
    "Population": 2300000,
    "Latitude": -22.328474,
    "Longitude": 24.684866
  },
  {
    "Country": "Portugal",
    "Data_Year": 2016,
    "Happiness_Rank": 94,
    "Happiness_Score": 5.12,
    "Life_Expectancy": 81.5,
    "Population": 10300000,
    "Latitude": 39.399872,
    "Longitude": -8.224454
  },
  {
    "Country": "Portugal",
    "Data_Year": 2018,
    "Happiness_Rank": 77,
    "Happiness_Score": 5.41,
    "Life_Expectancy": 81.7,
    "Population": 10300000,
    "Latitude": 39.399872,
    "Longitude": -8.224454
  },
  {
    "Country": "Portugal",
    "Data_Year": 2017,
    "Happiness_Rank": 89,
    "Happiness_Score": 5.2,
    "Life_Expectancy": 81.4,
    "Population": 10300000,
    "Latitude": 39.399872,
    "Longitude": -8.224454
  },
  {
    "Country": "Portugal",
    "Data_Year": 2015,
    "Happiness_Rank": 88,
    "Happiness_Score": 5.1,
    "Life_Expectancy": 81.5,
    "Population": 10400000,
    "Latitude": 39.399872,
    "Longitude": -8.224454
  },
  {
    "Country": "India",
    "Data_Year": 2019,
    "Happiness_Rank": 133,
    "Happiness_Score": 4.19,
    "Life_Expectancy": 69.5,
    "Population": 1370000000,
    "Latitude": 20.593684,
    "Longitude": 78.96288
  },
  {
    "Country": "Puerto Rico",
    "Data_Year": 2016,
    "Happiness_Rank": 15,
    "Happiness_Score": 7.04,
    "Life_Expectancy": 79.49,
    "Population": 3283125,
    "Latitude": 18.2208,
    "Longitude": -66.5901
  },
  {
    "Country": "Mongolia",
    "Data_Year": 2019,
    "Happiness_Rank": 94,
    "Happiness_Score": 5.12,
    "Life_Expectancy": 69.3,
    "Population": 3230000,
    "Latitude": 46.862496,
    "Longitude": 103.846656
  },
  {
    "Country": "Qatar",
    "Data_Year": 2017,
    "Happiness_Rank": 35,
    "Happiness_Score": 6.38,
    "Life_Expectancy": 80.2,
    "Population": 2720000,
    "Latitude": 25.354826,
    "Longitude": 51.183884
  },
  {
    "Country": "Qatar",
    "Data_Year": 2018,
    "Happiness_Rank": 32,
    "Happiness_Score": 6.37,
    "Life_Expectancy": 80.3,
    "Population": 2780000,
    "Latitude": 25.354826,
    "Longitude": 51.183884
  },
  {
    "Country": "Qatar",
    "Data_Year": 2015,
    "Happiness_Rank": 28,
    "Happiness_Score": 6.61,
    "Life_Expectancy": 79.9,
    "Population": 2570000,
    "Latitude": 25.354826,
    "Longitude": 51.183884
  },
  {
    "Country": "Qatar",
    "Data_Year": 2016,
    "Happiness_Rank": 36,
    "Happiness_Score": 6.38,
    "Life_Expectancy": 80.1,
    "Population": 2650000,
    "Latitude": 25.354826,
    "Longitude": 51.183884
  },
  {
    "Country": "Ethiopia",
    "Data_Year": 2019,
    "Happiness_Rank": 127,
    "Happiness_Score": 4.35,
    "Life_Expectancy": 69.1,
    "Population": 112000000,
    "Latitude": 9.145,
    "Longitude": 40.489673
  },
  {
    "Country": "Romania",
    "Data_Year": 2018,
    "Happiness_Rank": 52,
    "Happiness_Score": 5.94,
    "Life_Expectancy": 75.3,
    "Population": 19500000,
    "Latitude": 45.943161,
    "Longitude": 24.96676
  },
  {
    "Country": "Romania",
    "Data_Year": 2015,
    "Happiness_Rank": 86,
    "Happiness_Score": 5.12,
    "Life_Expectancy": 75.1,
    "Population": 19900000,
    "Latitude": 45.943161,
    "Longitude": 24.96676
  },
  {
    "Country": "Romania",
    "Data_Year": 2016,
    "Happiness_Rank": 71,
    "Happiness_Score": 5.53,
    "Life_Expectancy": 75.2,
    "Population": 19800000,
    "Latitude": 45.943161,
    "Longitude": 24.96676
  },
  {
    "Country": "Romania",
    "Data_Year": 2017,
    "Happiness_Rank": 57,
    "Happiness_Score": 5.82,
    "Life_Expectancy": 75.2,
    "Population": 19700000,
    "Latitude": 45.943161,
    "Longitude": 24.96676
  },
  {
    "Country": "Myanmar",
    "Data_Year": 2019,
    "Happiness_Rank": 130,
    "Happiness_Score": 4.31,
    "Life_Expectancy": 69.1,
    "Population": 54000000,
    "Latitude": 21.9162,
    "Longitude": 95.956
  },
  {
    "Country": "Russia",
    "Data_Year": 2017,
    "Happiness_Rank": 49,
    "Happiness_Score": 5.96,
    "Life_Expectancy": 72.1,
    "Population": 146000000,
    "Latitude": 61.52401,
    "Longitude": 105.318756
  },
  {
    "Country": "Russia",
    "Data_Year": 2018,
    "Happiness_Rank": 59,
    "Happiness_Score": 5.81,
    "Life_Expectancy": 72.3,
    "Population": 146000000,
    "Latitude": 61.52401,
    "Longitude": 105.318756
  },
  {
    "Country": "Russia",
    "Data_Year": 2016,
    "Happiness_Rank": 56,
    "Happiness_Score": 5.86,
    "Life_Expectancy": 71.8,
    "Population": 145000000,
    "Latitude": 61.52401,
    "Longitude": 105.318756
  },
  {
    "Country": "Russia",
    "Data_Year": 2015,
    "Happiness_Rank": 64,
    "Happiness_Score": 5.72,
    "Life_Expectancy": 71.3,
    "Population": 145000000,
    "Latitude": 61.52401,
    "Longitude": 105.318756
  },
  {
    "Country": "Rwanda",
    "Data_Year": 2018,
    "Happiness_Rank": 151,
    "Happiness_Score": 3.41,
    "Life_Expectancy": 68.8,
    "Population": 12300000,
    "Latitude": -1.940278,
    "Longitude": 29.873888
  },
  {
    "Country": "Rwanda",
    "Data_Year": 2015,
    "Happiness_Rank": 154,
    "Happiness_Score": 3.46,
    "Life_Expectancy": 67.7,
    "Population": 11400000,
    "Latitude": -1.940278,
    "Longitude": 29.873888
  },
  {
    "Country": "Rwanda",
    "Data_Year": 2016,
    "Happiness_Rank": 152,
    "Happiness_Score": 3.52,
    "Life_Expectancy": 68,
    "Population": 11700000,
    "Latitude": -1.940278,
    "Longitude": 29.873888
  },
  {
    "Country": "Rwanda",
    "Data_Year": 2017,
    "Happiness_Rank": 151,
    "Happiness_Score": 3.47,
    "Life_Expectancy": 68.5,
    "Population": 12000000,
    "Latitude": -1.940278,
    "Longitude": 29.873888
  },
  {
    "Country": "Rwanda",
    "Data_Year": 2019,
    "Happiness_Rank": 151,
    "Happiness_Score": 3.41,
    "Life_Expectancy": 69.1,
    "Population": 12600000,
    "Latitude": -1.940278,
    "Longitude": 29.873888
  },
  {
    "Country": "Saudi Arabia",
    "Data_Year": 2018,
    "Happiness_Rank": 33,
    "Happiness_Score": 6.37,
    "Life_Expectancy": 77,
    "Population": 33700000,
    "Latitude": 23.8859,
    "Longitude": 45.0792
  },
  {
    "Country": "Saudi Arabia",
    "Data_Year": 2016,
    "Happiness_Rank": 34,
    "Happiness_Score": 6.38,
    "Life_Expectancy": 76.6,
    "Population": 32400000,
    "Latitude": 23.8859,
    "Longitude": 45.0792
  },
  {
    "Country": "Saudi Arabia",
    "Data_Year": 2017,
    "Happiness_Rank": 37,
    "Happiness_Score": 6.34,
    "Life_Expectancy": 76.9,
    "Population": 33100000,
    "Latitude": 23.8859,
    "Longitude": 45.0792
  },
  {
    "Country": "Saudi Arabia",
    "Data_Year": 2015,
    "Happiness_Rank": 35,
    "Happiness_Score": 6.41,
    "Life_Expectancy": 76.2,
    "Population": 31700000,
    "Latitude": 23.8859,
    "Longitude": 45.0792
  },
  {
    "Country": "Gabon",
    "Data_Year": 2019,
    "Happiness_Rank": 103,
    "Happiness_Score": 4.76,
    "Life_Expectancy": 69,
    "Population": 2170000,
    "Latitude": -0.803689,
    "Longitude": 11.609444
  },
  {
    "Country": "Senegal",
    "Data_Year": 2017,
    "Happiness_Rank": 115,
    "Happiness_Score": 4.53,
    "Life_Expectancy": 68,
    "Population": 15400000,
    "Latitude": 14.497401,
    "Longitude": -14.452362
  },
  {
    "Country": "Senegal",
    "Data_Year": 2019,
    "Happiness_Rank": 109,
    "Happiness_Score": 4.63,
    "Life_Expectancy": 68.6,
    "Population": 16300000,
    "Latitude": 14.497401,
    "Longitude": -14.452362
  },
  {
    "Country": "Senegal",
    "Data_Year": 2016,
    "Happiness_Rank": 128,
    "Happiness_Score": 4.22,
    "Life_Expectancy": 67.8,
    "Population": 15000000,
    "Latitude": 14.497401,
    "Longitude": -14.452362
  },
  {
    "Country": "Senegal",
    "Data_Year": 2018,
    "Happiness_Rank": 109,
    "Happiness_Score": 4.63,
    "Life_Expectancy": 68.3,
    "Population": 15900000,
    "Latitude": 14.497401,
    "Longitude": -14.452362
  },
  {
    "Country": "Senegal",
    "Data_Year": 2015,
    "Happiness_Rank": 142,
    "Happiness_Score": 3.9,
    "Life_Expectancy": 67.5,
    "Population": 14600000,
    "Latitude": 14.497401,
    "Longitude": -14.452362
  },
  {
    "Country": "Yemen",
    "Data_Year": 2019,
    "Happiness_Rank": 152,
    "Happiness_Score": 3.36,
    "Life_Expectancy": 68.1,
    "Population": 29200000,
    "Latitude": 15.552727,
    "Longitude": 48.516388
  },
  {
    "Country": "Serbia",
    "Data_Year": 2017,
    "Happiness_Rank": 73,
    "Happiness_Score": 5.39,
    "Life_Expectancy": 75.7,
    "Population": 8830000,
    "Latitude": 44.016521,
    "Longitude": 21.005859
  },
  {
    "Country": "Serbia",
    "Data_Year": 2016,
    "Happiness_Rank": 86,
    "Happiness_Score": 5.18,
    "Life_Expectancy": 75.5,
    "Population": 8850000,
    "Latitude": 44.016521,
    "Longitude": 21.005859
  },
  {
    "Country": "Serbia",
    "Data_Year": 2015,
    "Happiness_Rank": 87,
    "Happiness_Score": 5.12,
    "Life_Expectancy": 75.1,
    "Population": 8880000,
    "Latitude": 44.016521,
    "Longitude": 21.005859
  },
  {
    "Country": "Serbia",
    "Data_Year": 2018,
    "Happiness_Rank": 78,
    "Happiness_Score": 5.4,
    "Life_Expectancy": 75.9,
    "Population": 8800000,
    "Latitude": 44.016521,
    "Longitude": 21.005859
  },
  {
    "Country": "Sierra Leone",
    "Data_Year": 2018,
    "Happiness_Rank": 113,
    "Happiness_Score": 4.57,
    "Life_Expectancy": 60.9,
    "Population": 7650000,
    "Latitude": 8.4606,
    "Longitude": 11.7799
  },
  {
    "Country": "Sierra Leone",
    "Data_Year": 2016,
    "Happiness_Rank": 111,
    "Happiness_Score": 4.64,
    "Life_Expectancy": 59.8,
    "Population": 7330000,
    "Latitude": 8.4606,
    "Longitude": 11.7799
  },
  {
    "Country": "Sierra Leone",
    "Data_Year": 2017,
    "Happiness_Rank": 106,
    "Happiness_Score": 4.71,
    "Life_Expectancy": 60.4,
    "Population": 7490000,
    "Latitude": 8.4606,
    "Longitude": 11.7799
  },
  {
    "Country": "Tanzania",
    "Data_Year": 2019,
    "Happiness_Rank": 153,
    "Happiness_Score": 3.3,
    "Life_Expectancy": 67.7,
    "Population": 58000000,
    "Latitude": -6.369028,
    "Longitude": 34.888822
  },
  {
    "Country": "Sierra Leone",
    "Data_Year": 2015,
    "Happiness_Rank": 123,
    "Happiness_Score": 4.51,
    "Life_Expectancy": 58.5,
    "Population": 7170000,
    "Latitude": 8.4606,
    "Longitude": 11.7799
  },
  {
    "Country": "Singapore",
    "Data_Year": 2018,
    "Happiness_Rank": 34,
    "Happiness_Score": 6.34,
    "Life_Expectancy": 85,
    "Population": 5760000,
    "Latitude": 1.352083,
    "Longitude": 103.819836
  },
  {
    "Country": "Singapore",
    "Data_Year": 2015,
    "Happiness_Rank": 24,
    "Happiness_Score": 6.8,
    "Life_Expectancy": 84.4,
    "Population": 5590000,
    "Latitude": 1.352083,
    "Longitude": 103.819836
  },
  {
    "Country": "Singapore",
    "Data_Year": 2017,
    "Happiness_Rank": 26,
    "Happiness_Score": 6.57,
    "Life_Expectancy": 84.8,
    "Population": 5710000,
    "Latitude": 1.352083,
    "Longitude": 103.819836
  },
  {
    "Country": "Laos",
    "Data_Year": 2019,
    "Happiness_Rank": 110,
    "Happiness_Score": 4.62,
    "Life_Expectancy": 67.43,
    "Population": 7169455,
    "Latitude": 19.85627,
    "Longitude": 102.495496
  },
  {
    "Country": "Singapore",
    "Data_Year": 2016,
    "Happiness_Rank": 22,
    "Happiness_Score": 6.74,
    "Life_Expectancy": 84.7,
    "Population": 5650000,
    "Latitude": 1.352083,
    "Longitude": 103.819836
  },
  {
    "Country": "Pakistan",
    "Data_Year": 2019,
    "Happiness_Rank": 75,
    "Happiness_Score": 5.47,
    "Life_Expectancy": 67.2,
    "Population": 217000000,
    "Latitude": 30.375321,
    "Longitude": 69.345116
  },
  {
    "Country": "Slovakia",
    "Data_Year": 2017,
    "Happiness_Rank": 40,
    "Happiness_Score": 6.1,
    "Life_Expectancy": 77.22,
    "Population": 5447900,
    "Latitude": 48.669026,
    "Longitude": 19.699024
  },
  {
    "Country": "Slovakia",
    "Data_Year": 2016,
    "Happiness_Rank": 45,
    "Happiness_Score": 6.08,
    "Life_Expectancy": 77.03,
    "Population": 5442003,
    "Latitude": 48.669026,
    "Longitude": 19.699024
  },
  {
    "Country": "Slovakia",
    "Data_Year": 2015,
    "Happiness_Rank": 45,
    "Happiness_Score": 6,
    "Life_Expectancy": 76.83,
    "Population": 5435611,
    "Latitude": 48.669026,
    "Longitude": 19.699024
  },
  {
    "Country": "Slovakia",
    "Data_Year": 2018,
    "Happiness_Rank": 39,
    "Happiness_Score": 6.17,
    "Life_Expectancy": 77.39,
    "Population": 5453014,
    "Latitude": 48.669026,
    "Longitude": 19.699024
  },
  {
    "Country": "Slovenia",
    "Data_Year": 2015,
    "Happiness_Rank": 55,
    "Happiness_Score": 5.85,
    "Life_Expectancy": 80.8,
    "Population": 2070000,
    "Latitude": 46.151241,
    "Longitude": 14.995463
  },
  {
    "Country": "Slovenia",
    "Data_Year": 2017,
    "Happiness_Rank": 62,
    "Happiness_Score": 5.76,
    "Life_Expectancy": 81.1,
    "Population": 2080000,
    "Latitude": 46.151241,
    "Longitude": 14.995463
  },
  {
    "Country": "Namibia",
    "Data_Year": 2019,
    "Happiness_Rank": 119,
    "Happiness_Score": 4.44,
    "Life_Expectancy": 67.2,
    "Population": 2490000,
    "Latitude": -22.95764,
    "Longitude": 18.49041
  },
  {
    "Country": "Slovenia",
    "Data_Year": 2016,
    "Happiness_Rank": 63,
    "Happiness_Score": 5.77,
    "Life_Expectancy": 81,
    "Population": 2070000,
    "Latitude": 46.151241,
    "Longitude": 14.995463
  },
  {
    "Country": "Slovenia",
    "Data_Year": 2018,
    "Happiness_Rank": 51,
    "Happiness_Score": 5.95,
    "Life_Expectancy": 81.3,
    "Population": 2080000,
    "Latitude": 46.151241,
    "Longitude": 14.995463
  },
  {
    "Country": "Somalia",
    "Data_Year": 2017,
    "Happiness_Rank": 93,
    "Happiness_Score": 5.15,
    "Life_Expectancy": 58.5,
    "Population": 14600000,
    "Latitude": 5.152149,
    "Longitude": 46.199616
  },
  {
    "Country": "Somalia",
    "Data_Year": 2018,
    "Happiness_Rank": 98,
    "Happiness_Score": 4.98,
    "Life_Expectancy": 58.9,
    "Population": 15000000,
    "Latitude": 5.152149,
    "Longitude": 46.199616
  },
  {
    "Country": "South Africa",
    "Data_Year": 2019,
    "Happiness_Rank": 105,
    "Happiness_Score": 4.72,
    "Life_Expectancy": 66.9,
    "Population": 58600000,
    "Latitude": 30.5595,
    "Longitude": 22.9375
  },
  {
    "Country": "Somalia",
    "Data_Year": 2016,
    "Happiness_Rank": 76,
    "Happiness_Score": 5.44,
    "Life_Expectancy": 58.5,
    "Population": 14200000,
    "Latitude": 5.152149,
    "Longitude": 46.199616
  },
  {
    "Country": "Somaliland Region",
    "Data_Year": 2016,
    "Happiness_Rank": 97,
    "Happiness_Score": 5.06,
    "Life_Expectancy": 55.15,
    "Population": 14185636,
    "Latitude": 9.562389,
    "Longitude": 44.077011
  },
  {
    "Country": "Somaliland region",
    "Data_Year": 2015,
    "Happiness_Rank": 91,
    "Happiness_Score": 5.06,
    "Life_Expectancy": 55.06,
    "Population": 13797201,
    "Latitude": 9.562389,
    "Longitude": 44.077011
  },
  {
    "Country": "South Africa",
    "Data_Year": 2018,
    "Happiness_Rank": 105,
    "Happiness_Score": 4.72,
    "Life_Expectancy": 66.6,
    "Population": 57800000,
    "Latitude": 30.5595,
    "Longitude": 22.9375
  },
  {
    "Country": "South Africa",
    "Data_Year": 2015,
    "Happiness_Rank": 113,
    "Happiness_Score": 4.64,
    "Life_Expectancy": 63.4,
    "Population": 55400000,
    "Latitude": 30.5595,
    "Longitude": 22.9375
  },
  {
    "Country": "Kenya",
    "Data_Year": 2019,
    "Happiness_Rank": 124,
    "Happiness_Score": 4.41,
    "Life_Expectancy": 66.7,
    "Population": 52600000,
    "Latitude": -0.023559,
    "Longitude": 37.906193
  },
  {
    "Country": "South Africa",
    "Data_Year": 2016,
    "Happiness_Rank": 116,
    "Happiness_Score": 4.46,
    "Life_Expectancy": 64.4,
    "Population": 56200000,
    "Latitude": 30.5595,
    "Longitude": 22.9375
  },
  {
    "Country": "South Africa",
    "Data_Year": 2017,
    "Happiness_Rank": 101,
    "Happiness_Score": 4.83,
    "Life_Expectancy": 66.3,
    "Population": 57000000,
    "Latitude": 30.5595,
    "Longitude": 22.9375
  },
  {
    "Country": "South Korea",
    "Data_Year": 2015,
    "Happiness_Rank": 47,
    "Happiness_Score": 5.98,
    "Life_Expectancy": 82.3,
    "Population": 50800000,
    "Latitude": 35.9078,
    "Longitude": 127.7669
  },
  {
    "Country": "South Korea",
    "Data_Year": 2017,
    "Happiness_Rank": 55,
    "Happiness_Score": 5.84,
    "Life_Expectancy": 82.6,
    "Population": 51100000,
    "Latitude": 35.9078,
    "Longitude": 127.7669
  },
  {
    "Country": "South Korea",
    "Data_Year": 2016,
    "Happiness_Rank": 57,
    "Happiness_Score": 5.84,
    "Life_Expectancy": 82.5,
    "Population": 51000000,
    "Latitude": 35.9078,
    "Longitude": 127.7669
  },
  {
    "Country": "Uganda",
    "Data_Year": 2019,
    "Happiness_Rank": 135,
    "Happiness_Score": 4.16,
    "Life_Expectancy": 66.6,
    "Population": 44300000,
    "Latitude": 1.373333,
    "Longitude": 32.290275
  },
  {
    "Country": "South Korea",
    "Data_Year": 2018,
    "Happiness_Rank": 57,
    "Happiness_Score": 5.88,
    "Life_Expectancy": 82.8,
    "Population": 51200000,
    "Latitude": 35.9078,
    "Longitude": 127.7669
  },
  {
    "Country": "South Sudan",
    "Data_Year": 2016,
    "Happiness_Rank": 143,
    "Happiness_Score": 3.83,
    "Life_Expectancy": 59.4,
    "Population": 10800000,
    "Latitude": 6.877,
    "Longitude": 31.307
  },
  {
    "Country": "South Sudan",
    "Data_Year": 2018,
    "Happiness_Rank": 154,
    "Happiness_Score": 3.25,
    "Life_Expectancy": 59.5,
    "Population": 11000000,
    "Latitude": 6.877,
    "Longitude": 31.307
  },
  {
    "Country": "Ghana",
    "Data_Year": 2019,
    "Happiness_Rank": 108,
    "Happiness_Score": 4.66,
    "Life_Expectancy": 66.1,
    "Population": 30400000,
    "Latitude": 7.946527,
    "Longitude": -1.023194
  },
  {
    "Country": "South Sudan",
    "Data_Year": 2017,
    "Happiness_Rank": 147,
    "Happiness_Score": 3.59,
    "Life_Expectancy": 59.3,
    "Population": 10900000,
    "Latitude": 6.877,
    "Longitude": 31.307
  },
  {
    "Country": "Spain",
    "Data_Year": 2016,
    "Happiness_Rank": 37,
    "Happiness_Score": 6.36,
    "Life_Expectancy": 82.9,
    "Population": 46600000,
    "Latitude": 40.463667,
    "Longitude": -3.74922
  },
  {
    "Country": "Spain",
    "Data_Year": 2015,
    "Happiness_Rank": 36,
    "Happiness_Score": 6.33,
    "Life_Expectancy": 82.6,
    "Population": 46700000,
    "Latitude": 40.463667,
    "Longitude": -3.74922
  },
  {
    "Country": "Spain",
    "Data_Year": 2017,
    "Happiness_Rank": 34,
    "Happiness_Score": 6.4,
    "Life_Expectancy": 83.1,
    "Population": 46600000,
    "Latitude": 40.463667,
    "Longitude": -3.74922
  },
  {
    "Country": "Haiti",
    "Data_Year": 2019,
    "Happiness_Rank": 148,
    "Happiness_Score": 3.58,
    "Life_Expectancy": 65.7,
    "Population": 11300000,
    "Latitude": 18.971187,
    "Longitude": -72.285215
  },
  {
    "Country": "Spain",
    "Data_Year": 2018,
    "Happiness_Rank": 36,
    "Happiness_Score": 6.31,
    "Life_Expectancy": 83.2,
    "Population": 46700000,
    "Latitude": 40.463667,
    "Longitude": -3.74922
  },
  {
    "Country": "Sri Lanka",
    "Data_Year": 2017,
    "Happiness_Rank": 120,
    "Happiness_Score": 4.44,
    "Life_Expectancy": 77.5,
    "Population": 21100000,
    "Latitude": 7.8731,
    "Longitude": 80.7718
  },
  {
    "Country": "Sri Lanka",
    "Data_Year": 2015,
    "Happiness_Rank": 132,
    "Happiness_Score": 4.27,
    "Life_Expectancy": 76.9,
    "Population": 20900000,
    "Latitude": 7.8731,
    "Longitude": 80.7718
  },
  {
    "Country": "Benin",
    "Data_Year": 2019,
    "Happiness_Rank": 136,
    "Happiness_Score": 4.14,
    "Life_Expectancy": 65.3,
    "Population": 11800000,
    "Latitude": 9.30769,
    "Longitude": 2.315834
  },
  {
    "Country": "Sri Lanka",
    "Data_Year": 2018,
    "Happiness_Rank": 116,
    "Happiness_Score": 4.47,
    "Life_Expectancy": 77.6,
    "Population": 21200000,
    "Latitude": 7.8731,
    "Longitude": 80.7718
  },
  {
    "Country": "Sri Lanka",
    "Data_Year": 2016,
    "Happiness_Rank": 117,
    "Happiness_Score": 4.42,
    "Life_Expectancy": 77.2,
    "Population": 21000000,
    "Latitude": 7.8731,
    "Longitude": 80.7718
  },
  {
    "Country": "Sudan",
    "Data_Year": 2018,
    "Happiness_Rank": 137,
    "Happiness_Score": 4.14,
    "Life_Expectancy": 70.5,
    "Population": 41800000,
    "Latitude": 12.862807,
    "Longitude": 30.217636
  },
  {
    "Country": "Nigeria",
    "Data_Year": 2019,
    "Happiness_Rank": 91,
    "Happiness_Score": 5.16,
    "Life_Expectancy": 65.2,
    "Population": 201000000,
    "Latitude": 9.081999,
    "Longitude": 8.675277
  },
  {
    "Country": "Sudan",
    "Data_Year": 2016,
    "Happiness_Rank": 133,
    "Happiness_Score": 4.14,
    "Life_Expectancy": 69.8,
    "Population": 39800000,
    "Latitude": 12.862807,
    "Longitude": 30.217636
  },
  {
    "Country": "Sudan",
    "Data_Year": 2015,
    "Happiness_Rank": 118,
    "Happiness_Score": 4.55,
    "Life_Expectancy": 69.6,
    "Population": 38900000,
    "Latitude": 12.862807,
    "Longitude": 30.217636
  },
  {
    "Country": "Sudan",
    "Data_Year": 2017,
    "Happiness_Rank": 130,
    "Happiness_Score": 4.14,
    "Life_Expectancy": 70.3,
    "Population": 40800000,
    "Latitude": 12.862807,
    "Longitude": 30.217636
  },
  {
    "Country": "Suriname",
    "Data_Year": 2015,
    "Happiness_Rank": 40,
    "Happiness_Score": 6.27,
    "Life_Expectancy": 71.9,
    "Population": 559000,
    "Latitude": 3.919305,
    "Longitude": -56.027783
  },
  {
    "Country": "Suriname",
    "Data_Year": 2016,
    "Happiness_Rank": 40,
    "Happiness_Score": 6.27,
    "Life_Expectancy": 71.9,
    "Population": 565000,
    "Latitude": 3.919305,
    "Longitude": -56.027783
  },
  {
    "Country": "Swaziland",
    "Data_Year": 2015,
    "Happiness_Rank": 101,
    "Happiness_Score": 4.87,
    "Life_Expectancy": 55.8,
    "Population": 1100000,
    "Latitude": -26.522503,
    "Longitude": 31.465866
  },
  {
    "Country": "Sweden",
    "Data_Year": 2018,
    "Happiness_Rank": 9,
    "Happiness_Score": 7.31,
    "Life_Expectancy": 82.6,
    "Population": 9970000,
    "Latitude": 60.128161,
    "Longitude": 18.643501
  },
  {
    "Country": "Sweden",
    "Data_Year": 2015,
    "Happiness_Rank": 8,
    "Happiness_Score": 7.36,
    "Life_Expectancy": 82.2,
    "Population": 9760000,
    "Latitude": 60.128161,
    "Longitude": 18.643501
  },
  {
    "Country": "Liberia",
    "Data_Year": 2019,
    "Happiness_Rank": 149,
    "Happiness_Score": 3.5,
    "Life_Expectancy": 65.2,
    "Population": 4940000,
    "Latitude": 6.428055,
    "Longitude": -9.429499
  },
  {
    "Country": "Sweden",
    "Data_Year": 2017,
    "Happiness_Rank": 9,
    "Happiness_Score": 7.28,
    "Life_Expectancy": 82.5,
    "Population": 9900000,
    "Latitude": 60.128161,
    "Longitude": 18.643501
  },
  {
    "Country": "Sweden",
    "Data_Year": 2016,
    "Happiness_Rank": 10,
    "Happiness_Score": 7.29,
    "Life_Expectancy": 82.4,
    "Population": 9840000,
    "Latitude": 60.128161,
    "Longitude": 18.643501
  },
  {
    "Country": "Togo",
    "Data_Year": 2019,
    "Happiness_Rank": 139,
    "Happiness_Score": 4,
    "Life_Expectancy": 65,
    "Population": 8080000,
    "Latitude": 8.619543,
    "Longitude": 0.824782
  },
  {
    "Country": "Switzerland",
    "Data_Year": 2017,
    "Happiness_Rank": 4,
    "Happiness_Score": 7.49,
    "Life_Expectancy": 84,
    "Population": 8460000,
    "Latitude": 46.818188,
    "Longitude": 8.227512
  },
  {
    "Country": "Switzerland",
    "Data_Year": 2015,
    "Happiness_Rank": 1,
    "Happiness_Score": 7.59,
    "Life_Expectancy": 83.5,
    "Population": 8300000,
    "Latitude": 46.818188,
    "Longitude": 8.227512
  },
  {
    "Country": "Switzerland",
    "Data_Year": 2018,
    "Happiness_Rank": 5,
    "Happiness_Score": 7.49,
    "Life_Expectancy": 84.1,
    "Population": 8530000,
    "Latitude": 46.818188,
    "Longitude": 8.227512
  },
  {
    "Country": "Switzerland",
    "Data_Year": 2016,
    "Happiness_Rank": 2,
    "Happiness_Score": 7.51,
    "Life_Expectancy": 83.8,
    "Population": 8380000,
    "Latitude": 46.818188,
    "Longitude": 8.227512
  },
  {
    "Country": "Syria",
    "Data_Year": 2018,
    "Happiness_Rank": 150,
    "Happiness_Score": 3.46,
    "Life_Expectancy": 70.6,
    "Population": 16900000,
    "Latitude": 34.802075,
    "Longitude": 38.996815
  },
  {
    "Country": "Syria",
    "Data_Year": 2015,
    "Happiness_Rank": 156,
    "Happiness_Score": 3.01,
    "Life_Expectancy": 67.3,
    "Population": 18000000,
    "Latitude": 34.802075,
    "Longitude": 38.996815
  },
  {
    "Country": "Syria",
    "Data_Year": 2017,
    "Happiness_Rank": 152,
    "Happiness_Score": 3.46,
    "Life_Expectancy": 69.8,
    "Population": 17100000,
    "Latitude": 34.802075,
    "Longitude": 38.996815
  },
  {
    "Country": "Angola",
    "Data_Year": 2019,
    "Happiness_Rank": 142,
    "Happiness_Score": 3.8,
    "Life_Expectancy": 65,
    "Population": 31800000,
    "Latitude": -11.202692,
    "Longitude": 17.873887
  },
  {
    "Country": "Syria",
    "Data_Year": 2016,
    "Happiness_Rank": 156,
    "Happiness_Score": 3.07,
    "Life_Expectancy": 67.4,
    "Population": 17500000,
    "Latitude": 34.802075,
    "Longitude": 38.996815
  },
  {
    "Country": "Taiwan",
    "Data_Year": 2015,
    "Happiness_Rank": 38,
    "Happiness_Score": 6.3,
    "Life_Expectancy": 79.84,
    "Population": 23557477,
    "Latitude": 23.69781,
    "Longitude": 120.960515
  },
  {
    "Country": "Madagascar",
    "Data_Year": 2019,
    "Happiness_Rank": 143,
    "Happiness_Score": 3.77,
    "Life_Expectancy": 64.2,
    "Population": 27000000,
    "Latitude": -18.766947,
    "Longitude": 46.869107
  },
  {
    "Country": "Taiwan",
    "Data_Year": 2016,
    "Happiness_Rank": 34,
    "Happiness_Score": 6.38,
    "Life_Expectancy": 80.2,
    "Population": 23618200,
    "Latitude": 23.69781,
    "Longitude": 120.960515
  },
  {
    "Country": "Taiwan",
    "Data_Year": 2018,
    "Happiness_Rank": 26,
    "Happiness_Score": 6.44,
    "Life_Expectancy": 80.4,
    "Population": 23726460,
    "Latitude": 23.69781,
    "Longitude": 120.960515
  },
  {
    "Country": "Taiwan",
    "Data_Year": 2017,
    "Happiness_Rank": 33,
    "Happiness_Score": 6.42,
    "Life_Expectancy": 80,
    "Population": 23674546,
    "Latitude": 23.69782,
    "Longitude": 120.960516
  },
  {
    "Country": "Tajikistan",
    "Data_Year": 2018,
    "Happiness_Rank": 88,
    "Happiness_Score": 5.2,
    "Life_Expectancy": 70.5,
    "Population": 9100000,
    "Latitude": 38.861034,
    "Longitude": 71.276093
  },
  {
    "Country": "Malawi",
    "Data_Year": 2019,
    "Happiness_Rank": 147,
    "Happiness_Score": 3.59,
    "Life_Expectancy": 64.2,
    "Population": 18600000,
    "Latitude": -13.254308,
    "Longitude": 34.301525
  },
  {
    "Country": "Tajikistan",
    "Data_Year": 2015,
    "Happiness_Rank": 106,
    "Happiness_Score": 4.79,
    "Life_Expectancy": 70.2,
    "Population": 8450000,
    "Latitude": 38.861034,
    "Longitude": 71.276093
  },
  {
    "Country": "Tajikistan",
    "Data_Year": 2017,
    "Happiness_Rank": 96,
    "Happiness_Score": 5.04,
    "Life_Expectancy": 70.3,
    "Population": 8880000,
    "Latitude": 38.861034,
    "Longitude": 71.276093
  },
  {
    "Country": "Tajikistan",
    "Data_Year": 2016,
    "Happiness_Rank": 100,
    "Happiness_Score": 5,
    "Life_Expectancy": 70.2,
    "Population": 8660000,
    "Latitude": 38.861034,
    "Longitude": 71.276093
  },
  {
    "Country": "Tanzania",
    "Data_Year": 2018,
    "Happiness_Rank": 153,
    "Happiness_Score": 3.3,
    "Life_Expectancy": 67.3,
    "Population": 56300000,
    "Latitude": -6.369028,
    "Longitude": 34.888822
  },
  {
    "Country": "Tanzania",
    "Data_Year": 2017,
    "Happiness_Rank": 153,
    "Happiness_Score": 3.35,
    "Life_Expectancy": 66.7,
    "Population": 54700000,
    "Latitude": -6.369028,
    "Longitude": 34.888822
  },
  {
    "Country": "Tanzania",
    "Data_Year": 2016,
    "Happiness_Rank": 149,
    "Happiness_Score": 3.67,
    "Life_Expectancy": 66.2,
    "Population": 53000000,
    "Latitude": -6.369028,
    "Longitude": 34.888822
  },
  {
    "Country": "Afghanistan",
    "Data_Year": 2019,
    "Happiness_Rank": 145,
    "Happiness_Score": 3.63,
    "Life_Expectancy": 64.1,
    "Population": 38000000,
    "Latitude": 33.93911,
    "Longitude": 67.709953
  },
  {
    "Country": "Tanzania",
    "Data_Year": 2015,
    "Happiness_Rank": 146,
    "Happiness_Score": 3.78,
    "Life_Expectancy": 65.6,
    "Population": 51500000,
    "Latitude": -6.369028,
    "Longitude": 34.888822
  },
  {
    "Country": "Zambia",
    "Data_Year": 2019,
    "Happiness_Rank": 125,
    "Happiness_Score": 4.38,
    "Life_Expectancy": 64,
    "Population": 17900000,
    "Latitude": -13.133897,
    "Longitude": 27.849332
  },
  {
    "Country": "Thailand",
    "Data_Year": 2015,
    "Happiness_Rank": 34,
    "Happiness_Score": 6.46,
    "Life_Expectancy": 78.2,
    "Population": 68700000,
    "Latitude": 15.870032,
    "Longitude": 100.992541
  },
  {
    "Country": "Thailand",
    "Data_Year": 2017,
    "Happiness_Rank": 32,
    "Happiness_Score": 6.42,
    "Life_Expectancy": 78.1,
    "Population": 69200000,
    "Latitude": 15.870032,
    "Longitude": 100.992541
  },
  {
    "Country": "Thailand",
    "Data_Year": 2018,
    "Happiness_Rank": 46,
    "Happiness_Score": 6.07,
    "Life_Expectancy": 78.4,
    "Population": 69400000,
    "Latitude": 15.870032,
    "Longitude": 100.992541
  },
  {
    "Country": "Thailand",
    "Data_Year": 2016,
    "Happiness_Rank": 33,
    "Happiness_Score": 6.47,
    "Life_Expectancy": 78,
    "Population": 69000000,
    "Latitude": 15.870032,
    "Longitude": 100.992541
  },
  {
    "Country": "Togo",
    "Data_Year": 2017,
    "Happiness_Rank": 150,
    "Happiness_Score": 3.49,
    "Life_Expectancy": 64.4,
    "Population": 7700000,
    "Latitude": 8.619543,
    "Longitude": 0.824782
  },
  {
    "Country": "Cameroon",
    "Data_Year": 2019,
    "Happiness_Rank": 99,
    "Happiness_Score": 4.97,
    "Life_Expectancy": 63.8,
    "Population": 25900000,
    "Latitude": 7.369722,
    "Longitude": 12.354722
  },
  {
    "Country": "Togo",
    "Data_Year": 2016,
    "Happiness_Rank": 155,
    "Happiness_Score": 3.3,
    "Life_Expectancy": 63.5,
    "Population": 7510000,
    "Latitude": 8.619543,
    "Longitude": 0.824782
  },
  {
    "Country": "Togo",
    "Data_Year": 2015,
    "Happiness_Rank": 158,
    "Happiness_Score": 2.84,
    "Life_Expectancy": 62.8,
    "Population": 7320000,
    "Latitude": 8.619543,
    "Longitude": 0.824782
  },
  {
    "Country": "Togo",
    "Data_Year": 2018,
    "Happiness_Rank": 139,
    "Happiness_Score": 4,
    "Life_Expectancy": 64.7,
    "Population": 7890000,
    "Latitude": 8.619543,
    "Longitude": 0.824782
  },
  {
    "Country": "Niger",
    "Data_Year": 2019,
    "Happiness_Rank": 134,
    "Happiness_Score": 4.17,
    "Life_Expectancy": 63.2,
    "Population": 23300000,
    "Latitude": 17.607789,
    "Longitude": 8.081666
  },
  {
    "Country": "Trinidad and Tobago",
    "Data_Year": 2018,
    "Happiness_Rank": 38,
    "Happiness_Score": 6.19,
    "Life_Expectancy": 74.4,
    "Population": 1390000,
    "Latitude": 10.6918,
    "Longitude": -61.2225
  },
  {
    "Country": "Trinidad and Tobago",
    "Data_Year": 2017,
    "Happiness_Rank": 38,
    "Happiness_Score": 6.17,
    "Life_Expectancy": 74.2,
    "Population": 1380000,
    "Latitude": 10.6918,
    "Longitude": -61.2225
  },
  {
    "Country": "Trinidad and Tobago",
    "Data_Year": 2016,
    "Happiness_Rank": 43,
    "Happiness_Score": 6.17,
    "Life_Expectancy": 74.3,
    "Population": 1380000,
    "Latitude": 10.6918,
    "Longitude": -61.2225
  },
  {
    "Country": "Trinidad and Tobago",
    "Data_Year": 2015,
    "Happiness_Rank": 41,
    "Happiness_Score": 6.17,
    "Life_Expectancy": 74.4,
    "Population": 1370000,
    "Latitude": 10.6918,
    "Longitude": -61.2225
  },
  {
    "Country": "Tunisia",
    "Data_Year": 2018,
    "Happiness_Rank": 111,
    "Happiness_Score": 4.59,
    "Life_Expectancy": 78.5,
    "Population": 11600000,
    "Latitude": 33.886917,
    "Longitude": 9.537499
  },
  {
    "Country": "Tunisia",
    "Data_Year": 2017,
    "Happiness_Rank": 102,
    "Happiness_Score": 4.8,
    "Life_Expectancy": 78.3,
    "Population": 11400000,
    "Latitude": 33.886917,
    "Longitude": 9.537499
  },
  {
    "Country": "Mali",
    "Data_Year": 2019,
    "Happiness_Rank": 118,
    "Happiness_Score": 4.45,
    "Life_Expectancy": 62.9,
    "Population": 19700000,
    "Latitude": 17.570692,
    "Longitude": -3.996166
  },
  {
    "Country": "Tunisia",
    "Data_Year": 2016,
    "Happiness_Rank": 98,
    "Happiness_Score": 5.04,
    "Life_Expectancy": 78.1,
    "Population": 11300000,
    "Latitude": 33.886917,
    "Longitude": 9.537499
  },
  {
    "Country": "Tunisia",
    "Data_Year": 2015,
    "Happiness_Rank": 107,
    "Happiness_Score": 4.74,
    "Life_Expectancy": 77.9,
    "Population": 11200000,
    "Latitude": 33.886917,
    "Longitude": 9.537499
  },
  {
    "Country": "Turkey",
    "Data_Year": 2017,
    "Happiness_Rank": 69,
    "Happiness_Score": 5.5,
    "Life_Expectancy": 78.9,
    "Population": 81100000,
    "Latitude": 38.963745,
    "Longitude": 35.243322
  },
  {
    "Country": "Congo (Kinshasa)",
    "Data_Year": 2019,
    "Happiness_Rank": 132,
    "Happiness_Score": 4.24,
    "Life_Expectancy": 62.7,
    "Population": 84100000,
    "Latitude": 4.0383,
    "Longitude": 21.7587
  },
  {
    "Country": "Turkey",
    "Data_Year": 2016,
    "Happiness_Rank": 78,
    "Happiness_Score": 5.39,
    "Life_Expectancy": 78.6,
    "Population": 79800000,
    "Latitude": 38.963745,
    "Longitude": 35.243322
  },
  {
    "Country": "Turkey",
    "Data_Year": 2018,
    "Happiness_Rank": 74,
    "Happiness_Score": 5.48,
    "Life_Expectancy": 79.2,
    "Population": 82300000,
    "Latitude": 38.963745,
    "Longitude": 35.243322
  },
  {
    "Country": "Turkey",
    "Data_Year": 2015,
    "Happiness_Rank": 76,
    "Happiness_Score": 5.33,
    "Life_Expectancy": 78.3,
    "Population": 78500000,
    "Latitude": 38.963745,
    "Longitude": 35.243322
  },
  {
    "Country": "Turkmenistan",
    "Data_Year": 2017,
    "Happiness_Rank": 59,
    "Happiness_Score": 5.82,
    "Life_Expectancy": 70.1,
    "Population": 5760000,
    "Latitude": 38.969719,
    "Longitude": 59.556278
  },
  {
    "Country": "Turkmenistan",
    "Data_Year": 2015,
    "Happiness_Rank": 70,
    "Happiness_Score": 5.55,
    "Life_Expectancy": 69.8,
    "Population": 5570000,
    "Latitude": 38.969719,
    "Longitude": 59.556278
  },
  {
    "Country": "Turkmenistan",
    "Data_Year": 2018,
    "Happiness_Rank": 68,
    "Happiness_Score": 5.64,
    "Life_Expectancy": 70.2,
    "Population": 5850000,
    "Latitude": 38.969719,
    "Longitude": 59.556278
  },
  {
    "Country": "Burkina Faso",
    "Data_Year": 2019,
    "Happiness_Rank": 121,
    "Happiness_Score": 4.42,
    "Life_Expectancy": 62.5,
    "Population": 20300000,
    "Latitude": 12.2383,
    "Longitude": 1.5616
  },
  {
    "Country": "Turkmenistan",
    "Data_Year": 2016,
    "Happiness_Rank": 65,
    "Happiness_Score": 5.66,
    "Life_Expectancy": 70,
    "Population": 5660000,
    "Latitude": 38.969719,
    "Longitude": 59.556278
  },
  {
    "Country": "Uganda",
    "Data_Year": 2017,
    "Happiness_Rank": 133,
    "Happiness_Score": 4.08,
    "Life_Expectancy": 65.7,
    "Population": 41200000,
    "Latitude": 1.373333,
    "Longitude": 32.290275
  },
  {
    "Country": "Uganda",
    "Data_Year": 2016,
    "Happiness_Rank": 145,
    "Happiness_Score": 3.74,
    "Life_Expectancy": 65.2,
    "Population": 39600000,
    "Latitude": 1.373333,
    "Longitude": 32.290275
  },
  {
    "Country": "Burundi",
    "Data_Year": 2019,
    "Happiness_Rank": 156,
    "Happiness_Score": 2.9,
    "Life_Expectancy": 62.3,
    "Population": 11500000,
    "Latitude": -3.373056,
    "Longitude": 29.918886
  },
  {
    "Country": "Uganda",
    "Data_Year": 2015,
    "Happiness_Rank": 141,
    "Happiness_Score": 3.93,
    "Life_Expectancy": 64.5,
    "Population": 38200000,
    "Latitude": 1.373333,
    "Longitude": 32.290275
  },
  {
    "Country": "Uganda",
    "Data_Year": 2018,
    "Happiness_Rank": 135,
    "Happiness_Score": 4.16,
    "Life_Expectancy": 66.2,
    "Population": 42700000,
    "Latitude": 1.373333,
    "Longitude": 32.290275
  },
  {
    "Country": "Congo (Brazzaville)",
    "Data_Year": 2019,
    "Happiness_Rank": 114,
    "Happiness_Score": 4.56,
    "Life_Expectancy": 62.2,
    "Population": 4860000,
    "Latitude": 0.228,
    "Longitude": 15.8277
  },
  {
    "Country": "Ukraine",
    "Data_Year": 2017,
    "Happiness_Rank": 132,
    "Happiness_Score": 4.1,
    "Life_Expectancy": 70.5,
    "Population": 44500000,
    "Latitude": 48.379433,
    "Longitude": 31.16558
  },
  {
    "Country": "Ukraine",
    "Data_Year": 2015,
    "Happiness_Rank": 111,
    "Happiness_Score": 4.68,
    "Life_Expectancy": 69.2,
    "Population": 44900000,
    "Latitude": 48.379433,
    "Longitude": 31.16558
  },
  {
    "Country": "Ukraine",
    "Data_Year": 2016,
    "Happiness_Rank": 123,
    "Happiness_Score": 4.32,
    "Life_Expectancy": 69.6,
    "Population": 44700000,
    "Latitude": 48.379433,
    "Longitude": 31.16558
  },
  {
    "Country": "Ukraine",
    "Data_Year": 2018,
    "Happiness_Rank": 138,
    "Happiness_Score": 4.1,
    "Life_Expectancy": 70.7,
    "Population": 44200000,
    "Latitude": 48.379433,
    "Longitude": 31.16558
  },
  {
    "Country": "United Arab Emirates",
    "Data_Year": 2015,
    "Happiness_Rank": 20,
    "Happiness_Score": 6.9,
    "Life_Expectancy": 73.1,
    "Population": 9260000,
    "Latitude": 23.4241,
    "Longitude": 53.8478
  },
  {
    "Country": "United Arab Emirates",
    "Data_Year": 2016,
    "Happiness_Rank": 28,
    "Happiness_Score": 6.57,
    "Life_Expectancy": 73.2,
    "Population": 9360000,
    "Latitude": 23.4241,
    "Longitude": 53.8478
  },
  {
    "Country": "Zimbabwe",
    "Data_Year": 2019,
    "Happiness_Rank": 144,
    "Happiness_Score": 3.69,
    "Life_Expectancy": 62,
    "Population": 14600000,
    "Latitude": -19.015438,
    "Longitude": 29.154857
  },
  {
    "Country": "United Arab Emirates",
    "Data_Year": 2017,
    "Happiness_Rank": 21,
    "Happiness_Score": 6.65,
    "Life_Expectancy": 73.3,
    "Population": 9490000,
    "Latitude": 23.4241,
    "Longitude": 53.8478
  },
  {
    "Country": "United Arab Emirates",
    "Data_Year": 2018,
    "Happiness_Rank": 20,
    "Happiness_Score": 6.77,
    "Life_Expectancy": 73.5,
    "Population": 9630000,
    "Latitude": 23.4241,
    "Longitude": 53.8478
  },
  {
    "Country": "United Kingdom",
    "Data_Year": 2016,
    "Happiness_Rank": 23,
    "Happiness_Score": 6.72,
    "Life_Expectancy": 80.9,
    "Population": 66300000,
    "Latitude": 55.3781,
    "Longitude": 3.436
  },
  {
    "Country": "Guinea",
    "Data_Year": 2019,
    "Happiness_Rank": 140,
    "Happiness_Score": 3.96,
    "Life_Expectancy": 61.6,
    "Population": 12800000,
    "Latitude": 9.945587,
    "Longitude": -9.696645
  },
  {
    "Country": "United Kingdom",
    "Data_Year": 2017,
    "Happiness_Rank": 19,
    "Happiness_Score": 6.71,
    "Life_Expectancy": 81,
    "Population": 66700000,
    "Latitude": 55.3781,
    "Longitude": 3.436
  },
  {
    "Country": "United Kingdom",
    "Data_Year": 2018,
    "Happiness_Rank": 11,
    "Happiness_Score": 7.19,
    "Life_Expectancy": 81,
    "Population": 67100000,
    "Latitude": 55.3781,
    "Longitude": 3.436
  },
  {
    "Country": "United Kingdom",
    "Data_Year": 2015,
    "Happiness_Rank": 21,
    "Happiness_Score": 6.87,
    "Life_Expectancy": 81,
    "Population": 65900000,
    "Latitude": 55.3781,
    "Longitude": 3.436
  },
  {
    "Country": "United States",
    "Data_Year": 2017,
    "Happiness_Rank": 14,
    "Happiness_Score": 6.99,
    "Life_Expectancy": 78.6,
    "Population": 325000000,
    "Latitude": 37.0902,
    "Longitude": -95.7129
  },
  {
    "Country": "Sierra Leone",
    "Data_Year": 2019,
    "Happiness_Rank": 113,
    "Happiness_Score": 4.57,
    "Life_Expectancy": 61.3,
    "Population": 7810000,
    "Latitude": 8.4606,
    "Longitude": 11.7799
  },
  {
    "Country": "United States",
    "Data_Year": 2018,
    "Happiness_Rank": 18,
    "Happiness_Score": 6.89,
    "Life_Expectancy": 78.6,
    "Population": 327000000,
    "Latitude": 37.0902,
    "Longitude": -95.7129
  },
  {
    "Country": "United States",
    "Data_Year": 2015,
    "Happiness_Rank": 15,
    "Happiness_Score": 7.12,
    "Life_Expectancy": 78.8,
    "Population": 321000000,
    "Latitude": 37.0902,
    "Longitude": -95.7129
  },
  {
    "Country": "United States",
    "Data_Year": 2016,
    "Happiness_Rank": 13,
    "Happiness_Score": 7.1,
    "Life_Expectancy": 78.6,
    "Population": 323000000,
    "Latitude": 37.0902,
    "Longitude": -95.7129
  },
  {
    "Country": "Chad",
    "Data_Year": 2019,
    "Happiness_Rank": 131,
    "Happiness_Score": 4.3,
    "Life_Expectancy": 60.6,
    "Population": 15900000,
    "Latitude": 15.454166,
    "Longitude": 18.732207
  },
  {
    "Country": "Uruguay",
    "Data_Year": 2018,
    "Happiness_Rank": 31,
    "Happiness_Score": 6.38,
    "Life_Expectancy": 77.2,
    "Population": 3450000,
    "Latitude": -32.522779,
    "Longitude": -55.765835
  },
  {
    "Country": "Uruguay",
    "Data_Year": 2015,
    "Happiness_Rank": 32,
    "Happiness_Score": 6.48,
    "Life_Expectancy": 77,
    "Population": 3410000,
    "Latitude": -32.522779,
    "Longitude": -55.765835
  },
  {
    "Country": "Uruguay",
    "Data_Year": 2017,
    "Happiness_Rank": 28,
    "Happiness_Score": 6.45,
    "Life_Expectancy": 77,
    "Population": 3440000,
    "Latitude": -32.522779,
    "Longitude": -55.765835
  },
  {
    "Country": "Uruguay",
    "Data_Year": 2016,
    "Happiness_Rank": 29,
    "Happiness_Score": 6.54,
    "Life_Expectancy": 77,
    "Population": 3420000,
    "Latitude": -32.522779,
    "Longitude": -55.765835
  },
  {
    "Country": "Uzbekistan",
    "Data_Year": 2017,
    "Happiness_Rank": 47,
    "Happiness_Score": 5.97,
    "Life_Expectancy": 70.3,
    "Population": 32000000,
    "Latitude": 41.377491,
    "Longitude": 64.585262
  },
  {
    "Country": "Mozambique",
    "Data_Year": 2019,
    "Happiness_Rank": 123,
    "Happiness_Score": 4.42,
    "Life_Expectancy": 59.9,
    "Population": 30400000,
    "Latitude": -18.665695,
    "Longitude": 35.529562
  },
  {
    "Country": "Uzbekistan",
    "Data_Year": 2018,
    "Happiness_Rank": 44,
    "Happiness_Score": 6.1,
    "Life_Expectancy": 70.5,
    "Population": 32500000,
    "Latitude": 41.377491,
    "Longitude": 64.585262
  },
  {
    "Country": "Uzbekistan",
    "Data_Year": 2016,
    "Happiness_Rank": 49,
    "Happiness_Score": 5.99,
    "Life_Expectancy": 70.1,
    "Population": 31400000,
    "Latitude": 41.377491,
    "Longitude": 64.585262
  },
  {
    "Country": "Uzbekistan",
    "Data_Year": 2015,
    "Happiness_Rank": 44,
    "Happiness_Score": 6,
    "Life_Expectancy": 69.9,
    "Population": 30900000,
    "Latitude": 41.377491,
    "Longitude": 64.585262
  },
  {
    "Country": "South Sudan",
    "Data_Year": 2019,
    "Happiness_Rank": 154,
    "Happiness_Score": 3.25,
    "Life_Expectancy": 59.7,
    "Population": 11100000,
    "Latitude": 6.877,
    "Longitude": 31.307
  },
  {
    "Country": "Venezuela",
    "Data_Year": 2016,
    "Happiness_Rank": 44,
    "Happiness_Score": 6.08,
    "Life_Expectancy": 75.3,
    "Population": 29900000,
    "Latitude": 6.42375,
    "Longitude": -66.58973
  },
  {
    "Country": "Venezuela",
    "Data_Year": 2018,
    "Happiness_Rank": 102,
    "Happiness_Score": 4.81,
    "Life_Expectancy": 75.2,
    "Population": 28900000,
    "Latitude": 6.42375,
    "Longitude": -66.58973
  },
  {
    "Country": "Venezuela",
    "Data_Year": 2017,
    "Happiness_Rank": 82,
    "Happiness_Score": 5.25,
    "Life_Expectancy": 75.3,
    "Population": 29400000,
    "Latitude": 6.42375,
    "Longitude": -66.58973
  },
  {
    "Country": "Venezuela",
    "Data_Year": 2015,
    "Happiness_Rank": 23,
    "Happiness_Score": 6.81,
    "Life_Expectancy": 75,
    "Population": 30100000,
    "Latitude": 6.42375,
    "Longitude": -66.58973
  },
  {
    "Country": "Vietnam",
    "Data_Year": 2016,
    "Happiness_Rank": 96,
    "Happiness_Score": 5.06,
    "Life_Expectancy": 74.4,
    "Population": 93600000,
    "Latitude": 14.058324,
    "Longitude": 108.277199
  },
  {
    "Country": "Vietnam",
    "Data_Year": 2015,
    "Happiness_Rank": 75,
    "Happiness_Score": 5.36,
    "Life_Expectancy": 74.3,
    "Population": 92700000,
    "Latitude": 14.058324,
    "Longitude": 108.277199
  },
  {
    "Country": "Vietnam",
    "Data_Year": 2017,
    "Happiness_Rank": 94,
    "Happiness_Score": 5.07,
    "Life_Expectancy": 74.5,
    "Population": 94600000,
    "Latitude": 14.058324,
    "Longitude": 108.277199
  },
  {
    "Country": "Somalia",
    "Data_Year": 2019,
    "Happiness_Rank": 98,
    "Happiness_Score": 4.98,
    "Life_Expectancy": 59.2,
    "Population": 15400000,
    "Latitude": 5.152149,
    "Longitude": 46.199616
  },
  {
    "Country": "Vietnam",
    "Data_Year": 2018,
    "Happiness_Rank": 95,
    "Happiness_Score": 5.1,
    "Life_Expectancy": 74.6,
    "Population": 95500000,
    "Latitude": 14.058324,
    "Longitude": 108.277199
  },
  {
    "Country": "Yemen",
    "Data_Year": 2015,
    "Happiness_Rank": 136,
    "Happiness_Score": 4.08,
    "Life_Expectancy": 68.6,
    "Population": 26500000,
    "Latitude": 15.552727,
    "Longitude": 48.516388
  },
  {
    "Country": "Ivory Coast",
    "Data_Year": 2019,
    "Happiness_Rank": 107,
    "Happiness_Score": 4.67,
    "Life_Expectancy": 57.02,
    "Population": 25716544,
    "Latitude": 7.54,
    "Longitude": 5.5471
  },
  {
    "Country": "Yemen",
    "Data_Year": 2018,
    "Happiness_Rank": 152,
    "Happiness_Score": 3.36,
    "Life_Expectancy": 68.1,
    "Population": 28500000,
    "Latitude": 15.552727,
    "Longitude": 48.516388
  },
  {
    "Country": "Yemen",
    "Data_Year": 2016,
    "Happiness_Rank": 147,
    "Happiness_Score": 3.72,
    "Life_Expectancy": 68.1,
    "Population": 27200000,
    "Latitude": 15.552727,
    "Longitude": 48.516388
  },
  {
    "Country": "Yemen",
    "Data_Year": 2017,
    "Happiness_Rank": 146,
    "Happiness_Score": 3.59,
    "Life_Expectancy": 68.1,
    "Population": 27800000,
    "Latitude": 15.552727,
    "Longitude": 48.516388
  },
  {
    "Country": "Lesotho",
    "Data_Year": 2019,
    "Happiness_Rank": 141,
    "Happiness_Score": 3.81,
    "Life_Expectancy": 56.1,
    "Population": 2130000,
    "Latitude": -29.609988,
    "Longitude": 28.233608
  },
  {
    "Country": "Zambia",
    "Data_Year": 2018,
    "Happiness_Rank": 125,
    "Happiness_Score": 4.38,
    "Life_Expectancy": 63.7,
    "Population": 17400000,
    "Latitude": -13.133897,
    "Longitude": 27.849332
  },
  {
    "Country": "Zambia",
    "Data_Year": 2015,
    "Happiness_Rank": 85,
    "Happiness_Score": 5.13,
    "Life_Expectancy": 62,
    "Population": 15900000,
    "Latitude": -13.133897,
    "Longitude": 27.849332
  },
  {
    "Country": "Zambia",
    "Data_Year": 2017,
    "Happiness_Rank": 116,
    "Happiness_Score": 4.51,
    "Life_Expectancy": 63.2,
    "Population": 16900000,
    "Latitude": -13.133897,
    "Longitude": 27.849332
  },
  {
    "Country": "Zambia",
    "Data_Year": 2016,
    "Happiness_Rank": 106,
    "Happiness_Score": 4.8,
    "Life_Expectancy": 62.8,
    "Population": 16400000,
    "Latitude": -13.133897,
    "Longitude": 27.849332
  },
  {
    "Country": "Zimbabwe",
    "Data_Year": 2017,
    "Happiness_Rank": 138,
    "Happiness_Score": 3.88,
    "Life_Expectancy": 61.4,
    "Population": 14200000,
    "Latitude": -19.015438,
    "Longitude": 29.154857
  },
  {
    "Country": "Zimbabwe",
    "Data_Year": 2016,
    "Happiness_Rank": 131,
    "Happiness_Score": 4.19,
    "Life_Expectancy": 60.5,
    "Population": 14000000,
    "Latitude": -19.015438,
    "Longitude": 29.154857
  },
  {
    "Country": "Central African Republic",
    "Data_Year": 2019,
    "Happiness_Rank": 155,
    "Happiness_Score": 3.08,
    "Life_Expectancy": 52.9,
    "Population": 4750000,
    "Latitude": 6.6111,
    "Longitude": 20.9394
  },
  {
    "Country": "Zimbabwe",
    "Data_Year": 2015,
    "Happiness_Rank": 115,
    "Happiness_Score": 4.61,
    "Life_Expectancy": 59.6,
    "Population": 13800000,
    "Latitude": -19.015438,
    "Longitude": 29.154857
  },
  {
    "Country": "Zimbabwe",
    "Data_Year": 2018,
    "Happiness_Rank": 144,
    "Happiness_Score": 3.69,
    "Life_Expectancy": 61.7,
    "Population": 14400000,
    "Latitude": -19.015438,
    "Longitude": 29.154857
  }
])

print("Data Uploaded!")
