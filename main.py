from flask import Flask, request, jsonify
from algoliasearch.search_client import SearchClient
import os

app = Flask(__name__)

# إعداد Algolia من Environment Variables
ALGOLIA_APP_ID = os.environ.get("ALGOLIA_APP_ID")
ALGOLIA_SEARCH_KEY = os.environ.get("ALGOLIA_SEARCH_KEY")
ALGOLIA_INDEX = os.environ.get("ALGOLIA_INDEX")

client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_SEARCH_KEY)
index = client.init_index(ALGOLIA_INDEX)

@app.route("/")
def home():
    return "Algolia server is running 🚀"

@app.route("/search")
def search():
    query = request.args.get("q", "")
    results = index.search(query)
    return jsonify(results)
