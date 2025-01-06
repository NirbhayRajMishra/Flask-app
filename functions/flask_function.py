import os
from flask import Flask, jsonify
from netlify_lambda import handler

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    # Your search logic (reading data from Excel, etc.)
    return jsonify({"message": "Search result!"})

# Netlify's handler to call the Flask app
handler(app)
