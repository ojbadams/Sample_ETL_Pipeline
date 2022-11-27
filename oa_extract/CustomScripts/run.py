""" Quick script that makes an API call to TFL api and commits data to MySQL """
from datatransformer import get_data, json_transformer
from simplemysql import SimpleMysql
import pandas as pd

def get_bike_location_data() -> pd.DataFrame:
    """ Function to get Data from TFL """
    url = "https://api.tfl.gov.uk/BikePoint/"

    data = get_data.make_request(url)
    data, pk = json_transformer.JSONTransform(data,
                    ['commonName',
                        'lat', 'lon', 'id'],
                        ["id"])

    return data

def start_mysql_connection_and_save(data: pd.DataFrame):
    """ Start Connection to Commit data to Staging """
    conn = SimpleMysql(user="python", passwd = "12345", db="Staging", charset="utf8")
    conn.connect()
    conn.insertBatch("locations", data.to_dict(orient="records"))
    conn.callProcedure("proc_transform")
    conn.commit()


if __name__ == "__main__":
    site_data = get_bike_location_data()
    start_mysql_connection_and_save(site_data)
