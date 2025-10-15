# Flask Form Application

A simple Flask application with frontend and backend services that collects user data and stores it in MongoDB.

## Structure
- `frontend/` - Flask web interface with form
- `backend/` - Flask API that stores data in MongoDB

## Setup

### Prerequisites
- Python 3.x
- MongoDB

### Installation
1. Install dependencies:
```bash
# Frontend
cd frontend
pip install -r requirements.txt

# Backend  
cd ../backend
pip install -r requirements.txt
```

2. Create `.env` files:

**frontend/.env:**
```
BACKEND_URL=http://localhost:4000
```

**backend/.env:**
```
MONGO_URI=mongodb://localhost:27017
```

### Running
1. Start MongoDB service
2. Run backend:
```bash
cd backend
python app.py
```
3. Run frontend:
```bash
cd frontend  
python app.py
```

Access the application at `http://localhost:5000`

## Usage
Fill out the form with first name, last name, and address. Data is submitted to the backend and stored in MongoDB.
