import csv
import pymongo
from pymongo import MongoClient
import os

currentDir = os.getcwd()
file = currentDir+"/zips.csv"
client = MongoClient('localhost', 27017)
db = client.zips
zipLatLongs = db.xys


count = 0
with open(file) as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        zip ={
        "Zipcode": row[0],
        "LatLong":[row[1], row[2]]
        }
        zip_id = zipLatLongs.insert_one(zip).inserted_id
        print(zip_id)
