from flask import Flask, jsonify
import os

app = Flask(__name__)

postgres_host = os.environ.get('PGHOST')

@app.route('/')
def index():
   return postgres_host
   return 'kuch bhi'

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
