from flask import Flask, jsonify
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route('/movies')
def display_movies():
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'games' table
        query = "SELECT * FROM netflix_titles"
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the games dictionary as JSON
        return jsonify(movies_dict)

# @app.route('/movies/<int:year>')
# def display_movies_by_year(year):
#         # Create a connection to the SQLite database
#         conn = sqlite3.connect('netflix.db')

#         # Query the 'games' table
#         query = "SELECT * from netflix_titles where date_added = '?-01-01' AND '?-12-31' "
#         df = pd.read_sql_query(query, conn, params=(year,))

#         # Close the connection
#         conn.close()

#         # Convert the DataFrame to a dictionary to make it easier to work with in Flask
#         movies_dict = df.to_dict('records')

#         # Return the games dictionary as JSON
#         return jsonify(movies_dict)

@app.route('/movies/<int:start_year>')
def display_movies_by_start_year(start_year):
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'games' table
        query = "SELECT * from netflix_titles where date_added >= ?"
        df = pd.read_sql_query(query, conn, params=(start_year,))

        # Close the connection
        conn.close()

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the games dictionary as JSON
        return jsonify(movies_dict)

@app.route('/stocks/<int:start>/<int:end>')
def display_stocks_by_start_year(start,end):
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'games' table
        query = "SELECT * from nflx where Date BETWEEN ?-01-01 AND ?-12-31 "
        df = pd.read_sql_query(query, conn, params=(start,end))

        # Close the connection
        conn.close()

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the games dictionary as JSON
        return jsonify(movies_dict)


@app.route('/stocks/')
def display_stocks():
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'games' table
        query = "SELECT * from nflx"
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the games dictionary as JSON
        return jsonify(movies_dict)


@app.route('/movies/test')
def test():
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'games' table
        query = "SELECT * from netflix_titles where date_added = 'September 24, 2021' "
        df = pd.read_sql_query(query, conn)

        # Close the connection
        conn.close()

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the games dictionary as JSON
        return jsonify(movies_dict)




if __name__ == "__main__":
        app.run(debug=True)