import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine

# Create a FastAPI instance
app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Create a SQLAlchemy engine to connect to the PostgreSQL database
engine = create_engine("postgresql://postgres:postgres@localhost:5432/pokemon")


# Define a route to fetch data from the database
@app.get("/pokemon")
def get_pokemon():
    # Connect to the database
    with engine.connect() as connection:
        # Execute a SQL query to fetch data from the database
        query = "SELECT * FROM basic_details"
        df = pd.read_sql(query, engine)

        # Convert the DataFrame to a JSON response
        response = df.to_json(orient="records", force_ascii=False)
        print(response)
        return response


@app.get("/pokemon/{id}")
def get_pokemon_by_id(id: int):
    # Connect to the database
    with engine.connect() as connection:
        # Execute a SQL query to fetch data from the database
        query = f"SELECT * FROM basic_details WHERE pokedex_number = {id}"
        df = pd.read_sql(query, engine)

        # Check if any rows were returned
        if df.empty:
            return JSONResponse(
                content={"message": "Pokemon not found"}, status_code=404
            )

        # Convert the DataFrame to a JSON response
        response = df.to_json(orient="records", force_ascii=False)
        return response
    

