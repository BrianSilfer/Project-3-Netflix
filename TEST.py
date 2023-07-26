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

@app.route('/movies/<int:year>')
def display_movies_by_year(year):
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'games' table
        query = "SELECT * from netflix_titles where date_added"
        df = pd.read_sql_query(query, conn, params=(year,))

        # Close the connection
        conn.close()

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the games dictionary as JSON
        return jsonify(movies_dict)

@app.route('/movies/<int:start_year>')
def display_movies_by_start_year(year):
        # Create a connection to the SQLite database
        conn = sqlite3.connect('netflix.db')

        # Query the 'games' table
        query = "SELECT * from netflix_titles where release_year >= ?"
        df = pd.read_sql_query(query, conn, params=(year,))

        # Close the connection
        conn.close()

        # Convert the DataFrame to a dictionary to make it easier to work with in Flask
        movies_dict = df.to_dict('records')

        # Return the games dictionary as JSON
        return jsonify(movies_dict)

if __name__ == "__main__":
        app.run(debug=True)