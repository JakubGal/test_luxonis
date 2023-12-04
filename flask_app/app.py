from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_data():
    """
    Fetches data from the PostgreSQL database.

    Returns:
        A list of tuples containing the flat data (id, title, image_url).
    """
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(host='db', dbname='flats_db', user='luxonis', password='admin')
    cur = conn.cursor()

    # Execute a query to retrieve all rows from the 'flats' table
    cur.execute('SELECT * FROM flats')
    flats = cur.fetchall()

    # Close the cursor and the connection
    cur.close()
    conn.close()

    return flats

@app.route('/')
def index():
    """
    The main route of the web application.

    Fetches data from the database and renders it using the 'index.html' template.
    """
    flats = get_data()
    return render_template('index.html', flats=flats)

# Check if the script is executed directly (i.e., not imported)
if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=8080)
