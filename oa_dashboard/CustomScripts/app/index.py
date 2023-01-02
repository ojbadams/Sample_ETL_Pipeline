from locale import locale_alias
from app import app
from flask import render_template, jsonify, request, flash, url_for, session, redirect
from flask import request
import pandas as pd

import math
import string

from geojson import MultiPoint
from geojson import Feature, Point, FeatureCollection

@app.route("/get_stop_name", methods = ["GET"])
def get_stop_name():
    lat = request.args.get("lat")
    lng = request.args.get("lng")
    name =  app.config["TEST_DB"].query_name_for_lat_lng(float(lat), float(lng))
    name = name.lower()
    name = string.capwords(name)
    print(name)
    return jsonify(name)

## Login Screen
@app.route("/", methods = ["POST", "GET"])
def login():
    df = app.config["TEST_DB"].get_full_df()

    locations_list = df.values.tolist()
    locations_list = [(i[1], i[2]) for i in locations_list]
    
    features = [Feature(geometry=Point(i)) for i in locations_list]
    f_c = FeatureCollection(features)
    
    locations_list = MultiPoint(locations_list)

    return render_template("test.html", locations_list = f_c)
