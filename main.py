import os
from flask import Flask, request, jsonify
from algoliasearch.search_client import SearchClient

app = Flask(__name__)

# Environment variables
ALGOLIA_APP_ID = os.environ.get("ALGOLIA_APP_ID")
ALGOLIA_SEARCH_KEY = os.environ.get("ALGOLIA_SEARCH_KEY")
ALGOLIA_INDEX = os.environ.get("ALGOLIA_INDEX")

# Algolia client
client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_SEARCH_KEY)
index = client.init_index(ALGOLIA_INDEX)

@app.route("/")
def home():
    return "Algolia Cloud Run is working 🚀"

@app.route("/search")
def search():
    query = request.args.get("query", "")
    results = index.search(query)
    return jsonify(results)

if name == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )
