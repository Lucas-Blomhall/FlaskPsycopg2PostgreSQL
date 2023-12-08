# import os
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

# Database connection
database_url = "postgresql://postgres:Vanligt123!@localhost/hemnet"
client = psycopg2.connect(database_url)
db = client.cursor(cursor_factory=psycopg2.extras.DictCursor)


# Create table


table_name = "broker"


def create_table():
    create_todo_query = """"""


def create_tables():
    """
    Create any necessary tables in this function, you can choose yourself if you want to
    run it at start or not.
    """
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
    db.execute(create_broker)
    db.execute(create_category)
    db.execute(create_customer)
    db.execute(create_listing)
    db.execute(create_listing_customer)
    client.commit()
    print("Created table successfully in PostgreSQL")


# Check if the table exists
def check_if_exists(table_name):
    try:
        db.execute("""
                    SELECT EXISTS(
                    SELECT 1 FROM information_schema.tables
                    WHERE table_catalog = 'hemnet'
                    AND table_schema = 'public'
                    AND table_name = %s
                    );
                    """, (table_name,))
        return db.fetchone()[0]
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
    try:
        db.execute(
            "INSERT INTO listing (name, price, description, category_id, broker_id) VALUES (%s, %s, %s, %s, %s)", (name, price, description, category_id, broker_id))
        client.commit()
        print("Created listing successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        client.rollback()
        return False


# Delete a listing
def delete_listing(id):
    """Deletes a listing from the database."""
    try:
        db.execute(
            "DELETE FROM listing WHERE id = %s", (id,))
        client.commit()
        print("Deleted listing successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        client.rollback()
        return False


# Get a listing
def view_listing():
    """Retrieves details of a specific listing along with category and broker information."""
    # Implement the SQL query to retrieve listing details with JOIN
    try:
        db.execute("SELECT * FROM listing ORDER BY id ASC")
        print("Got all listing successfully")
        return db.fetchall()  # Den returnar alla todos
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


# Category: CRUD

# Create Category
def create_category(name):
    """Creates a new category in the database."""
    try:
        db.execute(
            "INSERT INTO category (name) VALUES (%s)", (name,))
        client.commit()
        print("Created category successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        client.rollback()
        return False


# Update a category by id
def update_category(id, name):
    """Updates an existing category."""
    try:
        db.execute(
            "Update category SET title = %s, description = %s, WHERE id = %s", (id, name))
        client.commit()
        print("Updated category by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


# broker: CRUD

# Create a broker
def create_broker(name, email, contact_info):
    """Creates a new broker in the database."""
    try:
        db.execute(
            "INSERT INTO broker (name, email, contact_info) VALUES (%s, %s, %s)", (name, email, contact_info))
        client.commit()
        print("Created category successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        client.rollback()
        return False


# Update a broker by id
def update_broker(id, name, email, contact_info):
    """Updates an existing broker."""
    try:
        db.execute(
            "Update broker SET name = %s, email = %s, contact_info = %s, WHERE id = %s", (id, name, email, contact_info))
        client.commit()
        print("Updated category by id successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        return False


# create a customer
def create_customer(name, email, contact_info):
    """Creates a new customer in the database."""
    try:
        db.execute(
            "INSERT INTO customer (name, email, contact_info) VALUES (%s, %s, %s)", (name, email, contact_info))
        client.commit()
        print("Created customer successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        client.rollback()
        return False


def delete_customer(id):
    """Deletes a customer from the database."""
    try:
        db.execute(
            "DELETE FROM customer WHERE id = %s", (id,))
        client.commit()
        print("Deleted customer successfully")
    except psycopg2.Error as e:
        print("Error: ", e)
        client.rollback()
        return False


def create_appointment(connection):
    """Creates a new viewing appointment."""
    pass


def remove_appointment(connection):
    """Removes an appointment."""
    pass


def update_appointment(connection):
    """
    Updates an appointment
    """
    pass


def view_appointments_for_customer(connection):
    """Retrieves all appointments for a specific customer."""
    pass


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
