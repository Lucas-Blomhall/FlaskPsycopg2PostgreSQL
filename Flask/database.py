# import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask

import psycopg2


def connect_db():
    """Establishes a connection to the database."""
    try:
        connection = psycopg2.connect(
            host="localhost", port="8080", database="hemnet", user="postgres", password="Vanligt123!")
        return connection
    except psycopg2.DatabaseError as e:
        print(f"Database connection failed: {e}")
        raise  # Raising the exception here to propagate it if needed
