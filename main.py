import os
from flask import Flask, jsonify
from algoliasearch.search.client import SearchClient
from algoliasearch.search_client import SearchClient
app = Flask(__name__)

ALGOLIA_APP_ID = os.environ.get("ALGOLIA_APP_ID")
ALGOLIA_SEARCH_KEY = os.environ.get("ALGOLIA_SEARCH_KEY")
ALGOLIA_INDEX = os.environ.get("ALGOLIA_INDEX")

client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_SEARCH_KEY)
index = client.init_index(ALGOLIA_INDEX)

@app.route("/")
def home():
    return "Algolia service is running 🚀"

@app.route("/search")
def search():
    results = index.search("test")
    return jsonify(results)

if name == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
