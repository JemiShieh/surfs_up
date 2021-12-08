# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Create database engine
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect database into classes
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session link from Python to database
session = Session(engine)

# Create new flask instance called app
app = Flask(__name__)

# Create flask route
@app.route('/')

# Create welcome function defining routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API! 
    Available Routes: 
    /api/v1.0/precipitation 
    /api/v1.0/stations 
    /api/v1.0/tobs 
    /api/v1.0/temp/start/end
    ''')
