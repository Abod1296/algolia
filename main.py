from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

ALGOLIA_APP_ID = os.environ.get("ALGOLIA_APP_ID")
ALGOLIA_SEARCH_KEY = os.environ.get("ALGOLIA_SEARCH_KEY")
ALGOLIA_INDEX = os.environ.get("ALGOLIA_INDEX")

@app.route("/")
def home():
    return "OK SERVER WORKING 🚀"

@app.route("/search")
def search():
    query = request.args.get("q", "test")

    url = f"https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/{ALGOLIA_INDEX}/query"

    headers = {
        "X-Algolia-Application-Id": ALGOLIA_APP_ID,
        "X-Algolia-API-Key": ALGOLIA_SEARCH_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "params": f"query={query}"
    }

    response = requests.post(url, json=payload, headers=headers)

    return jsonify(response.json())
