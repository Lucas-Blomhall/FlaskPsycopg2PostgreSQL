# import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv
import os

load_dotenv()
# Database connection
database_url = os.getenv("DATABASE_URL")


# jag gillar det här sättet men vi stänger inte våran cursor och det är inte så bra. Den används ändå i main.py?
# client = psycopg2.connect(database_url)
# db = client.cursor(cursor_factory=psycopg2.extras.DictCursor)


def get_db_connection():
    return psycopg2.connect(database_url, cursor_factory=psycopg2.extras.DictCursor)

# Create table


table_name = "broker"


def create_table():
    create_todo_query = """"""


def create_tables():
    """
    Create any necessary tables in this function, you can choose yourself if you want to
    run it at start or not.
    """
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            create_broker = """
            CREATE TABLE IF NOT EXISTS broker(
            id SERIAL PRIMARY KEY
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) CHECK(email LIKE '%@%') UNIQUE,
            contact_info VARCHAR(20)
            );
            """
            create_category = """
            CREATE TABLE IF NOT EXISTS category(
            id SERIAL PRIMARY KEY
            name VARCHAR(255) UNIQUE NOT NULL,
            );
            """
            create_customer = """
            CREATE TABLE IF NOT EXISTS customer(
            id SERIAL PRIMARY KEY
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) CHECK(email LIKE '%@%') UNIQUE,
            contact_info VARCHAR(20)
            );
            """
            create_listing = """
            CREATE TABLE IF NOT EXISTS listing(
            id SERIAL PRIMARY KEY
            name VARCHAR(255) NOT NULL,
            price INT NOT NULL,
            description VARCHAR(255),
            category_id INT REFERENCES category(id),
            broker_id INT REFERENCES category(id)    
            );
            """
            create_listing_customer = """
            CREATE TABLE IF NOT EXISTS listing_customer(
            listing_id INT,
            customer_id INT,
            appointments BOOLEAN,
            favorite_residence BOOLEAN
            PRIMARY KEY(listing_id, customer_id)
            );
            """
            try:
                cur.execute(create_broker)
                cur.execute(create_category)
                cur.execute(create_customer)
                cur.execute(create_listing)
                cur.execute(create_listing_customer)
                # extra table för favorit
                conn.commit()
                print("Created table successfully in PostgreSQL")
            except psycopg2.Error as e:
                print("Error: ", e)
                conn.rollback()
                return False


# Check if the table exists
def check_if_exists(table_name):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                            SELECT EXISTS(
                            SELECT 1 FROM information_schema.tables
                            WHERE table_catalog = 'hemnet'
                            AND table_schema = 'public'
                            AND table_name = %s
                            );
                            """, (table_name,))
                return cur.fetchone()[0]
            except psycopg2.Error as e:
                print("Error", e)
                return False


print(f"Table {table_name} exists: {check_if_exists(table_name)}")
if check_if_exists(table_name) == False:
    create_table()
else:
    print("Table already exists")

print(f"Table {table_name} exists: {check_if_exists(table_name)}")


# Starting CRUD:

# Listing: CRUD:

# Create a listing:
def create_listing(name, price, description, category_id, broker_id):
    """Creates a new listing in the database."""
    # Implement the SQL query to insert a new listing
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO listing (name, price, description, category_id, broker_id) VALUES (%s, %s, %s, %s, %s)", (name, price, description, category_id, broker_id))
                conn.commit()
                print("Created listing successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                conn.rollback()
                return False


# Delete a listing
def delete_listing(id):
    """Deletes a listing from the database."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "DELETE FROM listing WHERE id = %s", (id,))
                conn.commit()
                print("Deleted listing successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                conn.rollback()
                return False


# Get a listing
def view_listing():
    """Retrieves details of a specific listing along with category and broker information."""
    # Implement the SQL query to retrieve listing details with JOIN
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("SELECT * FROM listing ORDER BY id ASC")
                print("Got all listing successfully")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# Update a listing by id
def update_listing(id, name, price, description, category_id, broker_id):
    """Updates an existing listing."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "UPDATE listing SET name = %s, price = %s, description = %s, category_id = %s, broker_id = %s WHERE id = %s",
                    (name, price, description, category_id, broker_id, id))
                conn.commit()
                print("Updated listing by id successfully")
                return True
            except psycopg2.Error as e:
                print("Error: ", e)
                conn.rollback()
                return False


# # Get a listing by id kommer tillbaka och fixar för specifik id
# id SERIAL PRIMARY KEY
# name VARCHAR(255) NOT NULL,
# price INT NOT NULL,
# description VARCHAR(255),
# category_id INT REFERENCES category(id),
# broker_id INT REFERENCES category(id)
def view_listing_by_id(id):
    """Retrieves details of a specific listing along with category and broker information."""
    # Implement the SQL query to retrieve listing details with JOIN
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("SELECT * FROM listing WHERE id = %s", (id,))
                print("Got specific listing by id successfully")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# Category: CRUD

# Create Category
def create_category(name):
    """Creates a new category in the database."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO category (name) VALUES (%s)", (name,))
                conn.commit()
                print("Created category successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                conn.rollback()
                return False


# Update a category by id
def update_category(id, name):
    """Updates an existing category."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "Update category SET title = %s, description = %s, WHERE id = %s", (id, name))
                conn.commit()
                print("Updated category by id successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# broker: CRUD

# Create a broker
def create_broker(name, email, contact_info):
    """Creates a new broker in the database."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO broker (name, email, contact_info) VALUES (%s, %s, %s)", (name, email, contact_info))
                conn.commit()
                print("Created category successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                conn.rollback()
                return False


# Update a broker by id
def update_broker(id, name, email, contact_info):
    """Updates an existing broker."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "Update broker SET name = %s, email = %s, contact_info = %s, WHERE id = %s", (id, name, email, contact_info))
                conn.commit()
                print("Updated category by id successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


# create a customer
def create_customer(name, email, contact_info):
    """Creates a new customer in the database."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO customer (name, email, contact_info) VALUES (%s, %s, %s)", (name, email, contact_info))
                conn.commit()
                print("Created customer successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                conn.rollback()
                return False


# Read customer
def view_customer():
    """Retrieves details of a specific listing along with category and broker information."""
    # Implement the SQL query to retrieve listing details with JOIN
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("SELECT * FROM customer ORDER BY id ASC")
                print("Got all listing successfully")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False

# UPDATE customer


def delete_customer(id):
    """Deletes a customer from the database."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "DELETE FROM customer WHERE id = %s", (id,))
                conn.commit()
                print("Deleted customer successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                conn.rollback()
                return False


def create_appointment(listing_id, customer_id, appointments):
    """Creates a new viewing appointment."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "INSERT INTO listing_customer (listing_id, customer_id, appointments) VALUES (%s, %s)", (
                        listing_id, customer_id, appointments)
                )
                conn.commit()
                print("Created an appointment in listing_customer successfully")
            except psycopg2.Error as e:
                print("Error: ", e)
                conn.rollback()
                return False


def remove_appointment(listing_id, customer_id):
    """Removes an appointment."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "DELETE FROM listing_customer WHERE listing_id = %s AND customer_id = %s", (listing_id, customer_id))
                print("Deleted an appointment from listing_customer")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


def update_appointment(listing_id, customer_id, appointments):
    """Updates an appointment"""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "Update listing_customer SET appointments = %s, WHERE listing_id = %s AND customer_id = %s", (listing_id, customer_id, appointments))
                print("Update an appointment from listing_customer")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


def view_appointments_for_customer(listing_id, customer_id):
    """Retrieves all appointments for a specific customer."""
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    "SELECT * FROM listing_customer WHERE customer_id = %s", (listing_id, customer_id))
                print("Update an appointment from listing_customer")
                return cur.fetchall()  # Den returnar alla todos
            except psycopg2.Error as e:
                print("Error: ", e)
                return False


def favorite_listing(connection):
    """You can choose freely how to implement it"""
    pass


def unfavorite_listing(connection):
    """You can choose freely how to implement it"""
    pass


# def connect_db():
#     """Establishes a connection to the database."""
#     try:
#         connection = psycopg2.connect(
#             host="localhost", port="8080", database="hemnet", user="postgres", password="Vanligt123!")
#         return connection
#     except psycopg2.DatabaseError as e:
#         print(f"Database connection failed: {e}")
#         raise  # Raising the exception here to propagate it if needed
