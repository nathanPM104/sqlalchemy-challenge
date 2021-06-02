import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################


# create engine to hawaii.sqlite
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

@app.route("/")
def welcome():
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )


@app.route("/api/v1.0/precipitation")

def precipitation():
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= "2016-08-24").\
    filter(Measurement.date <= "2017-08-23").all()

    precip = {date: prcp for date, prcp in results}
    return jsonify(precip)
    

@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station, Station.name).order_by(Station.name.desc()).all()
    
    stations = list(np.ravel(results))
    return jsonify(stations)



@app.route("/api/v1.0/tobs")

def active_station():
    station = 'USC00511918'

    results = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
    filter(Measurement.station == station).\
    filter(Measurement.date >= "2014-10-30").\
    filter(Measurement.date <= "2015-10-30").all()
    
    station_temps = list(np.ravel(results))

    # Return the results
    return jsonify(temps)

@app.route("/api/v1.0/temp/start/end")

def temp

    
if __name__ == '__main__':
    app.run()