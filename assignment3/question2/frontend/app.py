# Flask frontend app - handles form submission and communicates with backend
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()
BACKEND_URL = os.getenv('BACKEND_URL')

app = Flask(__name__)

# Home page route
@app.route("/")
def home():
    return render_template("index.html")

# Form submission route - forwards data to backend
@app.route("/submit", methods=["POST"])
def submit():
    try:
        """
        # Test exception trigger
        if request.form.get("first_name") == "test":
            raise Exception("Error: Provide proper first name.")
        """
        
        # Convert form data to dict and send to backend
        form_data = dict(request.form)
        requests.post(f"{BACKEND_URL}/submit", json=form_data)
        return 'Data sumbitted successfully'
    except Exception as e:
        # Return error to user if submission fails
        error_message = str(e)
        return render_template("index.html", error=error_message)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
