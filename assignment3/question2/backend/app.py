# Flask backend app - receives data and stores in MongoDB
from flask import Flask,request
from dotenv import load_dotenv
import os
import pymongo

# Load environment variables
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

# MongoDB connection setup
client = pymongo.MongoClient(MONGO_URI)
db = client.assignment
collection = db['assignment_3']

app = Flask(__name__)

# Data submission endpoint - stores form data in MongoDB
@app.route("/submit", methods=["POST"]) 
def submit():
    # Extract JSON data and insert into database
    request_data = dict(request.json)
    collection.insert_one(request_data)
    return "Data submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)