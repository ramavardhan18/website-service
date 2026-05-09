# IT Startup Backend - FastAPI + PostgreSQL

## Setup

### Create Virtual Environment
python -m venv venv

### Activate Environment
Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

### Install Requirements
pip install -r requirements.txt

### Run Server
uvicorn app.main:app --reload

### Swagger Docs
http://127.0.0.1:8000/docs