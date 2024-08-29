## Installations

##### 1. Create virtual environment
`python3 -m venv .venv`

##### 2. Activate virtual environment
`source .venv/bin/activate`

##### 3. Install Fast API
`pip install fastapi`

##### 4. Install Uvicorn
`pip install "uvicorn[standard]"`

##### 5. Install SQLModel
`pip install sqlmodel`

## Running application
`uvicorn main:app --reload`

## API Documentation
1. http://localhost:8000/docs
2. http://localhost:8000/redoc
