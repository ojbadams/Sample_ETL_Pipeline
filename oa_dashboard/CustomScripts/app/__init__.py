from flask import Flask, request
from backend.database import DB

app = Flask(__name__, template_folder="templates")

app.config['SECRET_KEY'] = 'the random string' 
app.config["TEST_DB"] = DB()


from app import index
