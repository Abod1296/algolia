from flask import Flask
from algoliasearch.search_client import SearchClient
import os

app = Flask(__name__)

# Algolia config (نجيبهم من Environment Variables)
ALGOLIA_APP_ID = os.environ.get("ALGOLIA_APP_ID")
ALGOLIA_API_KEY = os.environ.get("ALGOLIA_API_KEY")
ALGOLIA_INDEX = os.environ.get("ALGOLIA_INDEX")

@app.route("/")
def home():
    return "Server is working ✅"

@app.route("/search")
def search():
    client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_API_KEY)
    index = client.init_index(ALGOLIA_INDEX)

    results = index.search("test")
    return results
