from flask import Flask, jsonify, request
from flask_cors import CORS
from .config import API_KEY

app = Flask(__name__)

CORS(app, resources = {r"/api/news": {
    "origins": ["https://mireziz-memmedov.github.io"],
    "methods": ["GET"]
}})

@app.route("/api/news", methods=["GET"])
def get_news():

    api_key = request.args.get("api_key")

    news = {"id": 1, "title": "Demo"}

    if api_key is None and len(request.args) > 0:
        return jsonify({"error": "Invalid query parametrs"})

    if api_key and api_key !=API_KEY:
        return jsonify({"error": "Invalid api key"})
        
    return jsonify({"news": news})     