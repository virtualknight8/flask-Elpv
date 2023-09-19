from flask import Flask, jsonify
import os

app = Flask(__name__)

postgres_host = os.environ.get('PGHOST')
purl = os.environ.get('DATABASE_URL')

@app.route('/')
def index():
   return { 'host' : postgres_host,
'url' : purl}

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
