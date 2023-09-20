from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

# Get PostgreSQL connection details from environment variables
postgres_host = os.environ.get('PGHOST')
postgres_port = os.environ.get('PGPORT')
postgres_db = os.environ.get('PGDATABASE')
postgres_user = os.environ.get('PGUSER')
postgres_password = os.environ.get('PGPASSWORD')

@app.route('/')
def index():
  # Create a connection to the PostgreSQL database
    try:
        conn = psycopg2.connect(
        host=postgres_host,
        port=postgres_port,
        database=postgres_db,
        user=postgres_user,
        password=postgres_password
    )

    # If the connection is successful, print a success message
        print("Connected to PostgreSQL successfully!")

    # Close the connection
        conn.close()

    except psycopg2.Error as e:
    # If there's an error, print an error message
        print("Error connecting to PostgreSQL:", e)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
