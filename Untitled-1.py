# Import the dependencies.
import numpy as np


from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import os
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
curr_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(curr_dir, 'netflix.db')
engine = create_engine(f"sqlite:///{db_path}")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

NFLXTable = Base.classes.nflx
nflxReleases = Base.classes.nflx_titles

# Create our session (link) from Python to the DB

session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"For following routes enter date in YYYY, YYYY-MM, or YYYY-MM-DD format:<br/>"
        f"/api/v1.0/start-date/end-date<br/>"
        f"For testing connections"
        f"/api/v1.0/test<br/>"

    )

@app.route("/api/v1.0/<start>/<end>")
def stock_start_end_route(start,end):
    """Return the stats of NFLX stocks for the specified dates"""
    

    start_results = session.query((NFLXTable.Date),
                                (NFLXTable.Open),
                                (NFLXTable.High),
                                (NFLXTable.Low),
                                (NFLXTable.Close)).\
                                filter(NFLXTable.Date >= start,NFLXTable.Date <= end).all()


    results = session.query(NFLXTable.Date,NFLXTable.Open,NFLXTable.High,NFLXTable.Low,NFLXTable.Close).all()

    #Close sesssion
    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_info = []
    for Date, Open, High, Low, Close in results:
        nflx_dict = {}
        nflx_dict["Date"] = Date
        nflx_dict["Open"] = Open
        nflx_dict["High"] = High
        nflx_dict["Low"] = Low
        nflx_dict["Close"] = Close
        all_info.append(nflx_dict)

    #Return results

    return jsonify(all_info)

    #Close session and return results

@app.route("/api/v1.0/test")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all station info"""
    # Query all stations
    results = session.query(NFLXTable.Date,NFLXTable.Open,NFLXTable.High,NFLXTable.Low,NFLXTable.Close).all()

    #Close sesssion
    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_info = []
    for Date, Open, High, Low, Close in results:
        nflx_dict = {}
        nflx_dict["Date"] = Date
        nflx_dict["Open"] = Open
        nflx_dict["High"] = High
        nflx_dict["Low"] = Low
        nflx_dict["Close"] = Close
        all_info.append(nflx_dict)


    #Return results

    return jsonify(all_info)



if __name__ == '__main__':
    app.run(debug=True)