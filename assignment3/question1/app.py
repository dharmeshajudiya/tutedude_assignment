# Flask assignment - Simple API to read JSON file
from flask import Flask

# Initialize Flask application
app = Flask(__name__)

# API endpoint to read and return sample.json content
@app.route('/api')
def home():
    # Open and read the JSON file
    file = open('sample.json', 'r')
    data = list(file.readlines())
    file.closed
    # Return data as JSON response
    return {"data": data}

# Run the Flask app on all interfaces, port 5000
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

