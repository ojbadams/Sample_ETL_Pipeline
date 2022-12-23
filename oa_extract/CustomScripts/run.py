""" Quick script that makes an API call to TFL api and commits data to MySQL """
from datetime import datetime
import pandas as pd
from pymongo import MongoClient
from datatransformer import get_data


def get_bike_location_data() -> pd.DataFrame:
    """ Function to get Data from TFL """
    url = "https://api.tfl.gov.uk/BikePoint/"

    data = get_data.make_request(url)
    data = {"inserted_date" : datetime.now(), "data" : data}
    return data

def save_data_to_mongo(data):
    """ Saves API output to MongoDB """
    client = MongoClient("localhost", 27017, username="root", password="password")
    data_base = client["staging"]
    collection = data_base["locations"]
    collection.insert_one(data)

if __name__ == "__main__":
    site_data = get_bike_location_data()
    save_data_to_mongo(site_data)
