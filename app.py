from flask import Flask, jsonify, request
from database import create_category, create_listing, update_listing, view_customer, view_listing, delete_listing, view_listing_by_id

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_todos():
    return jsonify({'message': "welcome to hemnet!"})


# Vi kör en foreach loop där vi kollar igenom alla värdena för  att kunna formatera värderna
# listing
def format_listing(listings):
    return [{
        'id': listing['id'],
        'name': listing['name'],
        'price': listing['price'],
        'description': listing['description'],
        'category_id': listing['category_id'],
        'broker_id': listing['broker_id']
    } for listing in listings]

# customer


def format_customer(customers):
    return [{
        'id': customer['id'],
        'name': customer['name'],
        'email': customer['email'],
        'contact_info': customer['contact_info']
    } for customer in customers]


# Create listing
@app.route('/listing', methods=['POST'])
def add_listing_route():
    """
    Endpoint to add a new listing
    """
    data = request.get_json()
    name = data['name']
    price = data['price']
    description = data['description']
    category_id = data['category_id']
    broker_id = data['broker_id']
    create_listing(name, price, description, category_id, broker_id)
    return jsonify({'message': "created listing successfully"}), 201


# Read listing
@app.route('/listing/<int:id>', methods=['GET'])
def listing_detail_route(id):
    """
    Endpoint to return a specific listing
    """
    selected_listing = view_listing_by_id(id)
    new_listing = format_listing(selected_listing)
    return jsonify(new_listing), 200


# Read listing
@app.route('/listing', methods=['GET'])
def get_all_listings_route():
    """
    Should return a list of X number of listings based on a LIMIT
    """
    listings = view_listing()
    new_listing = format_listing(listings)
    return jsonify(new_listing), 200


# Update listing
@app.route('/listing/<int:id>', methods=['PUT'])
def update_listing_route(id):
    """
    Endpoint to update an existing listing
    """
    data = request.get_json()  # Hämtar data från Postman
    name = data['name']
    price = data['price']
    description = data['description']
    category_id = data['category_id']
    broker_id = data['broker_id']

    success = update_listing(
        id, name, price, description, category_id, broker_id)

    if success == True:
        return jsonify({'message': "Updated listing successfully"}), 200
    else:
        return jsonify({'message': "Failed to update listing"}), 400


# Delete listing
@app.route('/listing/<id>', methods=['DELETE'])
def remove_listing_route(id):
    """
    Endpoint to remove a listing
    """
    delete_listing(id)
    return jsonify({'message': "deleted listing successfully"}), 200


@app.route('/category', methods=['POST'])
def add_category_route():
    """
    Endpoint to add a new category
    Get category details from customer and call db.create_category
    """
    data = request.get_json()
    name = data['name']
    create_category(name)
    return jsonify({'message': "created listing successfully"}), 201


def add_category():

    pass


@app.route('/category/<int:id>', methods=['PUT'])
def update_category_route():
    """
    Endpoint to update a category
    Get updated category details from customer and call db.update_category
    """
    data = request.get_json()

    selected_category = view_listing_by_id(id)
    new_category = format_listing(selected_category)
    return jsonify(new_category), 200


# # Update single listing
# @app.route('/listing/<int:id>', methods=['PUT'])
# def update_listing_route(id):
#     data = request.get_json()
#     selected_listing = view_listing_by_id(id)
#     new_listing = format_listing(selected_listing)
#     return jsonify(new_listing), 200


def add_broker():
    """
    Endpoint to add a new broker
    Get broker details from customer and call db.create_broker
    """
    pass


def modify_broker():
    """
    Endpoint to modify a broker
    Get updated broker details from customer and call db.update_broker
    """
    pass


def add_customer():
    """
    Endpoint to add a new customer
    Get customer details from customer and call db.create_customer
    """
    pass


def remove_customer():
    """
    Endpoint to remove a customer
    Get customer ID from customer and call db.delete_customer
    """
    pass


@app.route('/customer', methods=['GET'])
def get_all_customer_route():
    """
    Endpoint to list all customer
    """
    customers = view_customer()
    new_customer = format_customer(customers)
    return jsonify(new_customer), 200


def schedule_appointment():
    """
    Endpoint to schedule a viewing appointment
    Get appointment details from customer and call db.create_appointment
    """
    pass


def update_appointment():
    """
    Endpoint to update an existing appointment
    Get appointment details from customer and call db.update_appointment
    """
    pass


def cancel_appointment():
    """
    Endpoint to cancel an appointment
    Get appointment ID from customer and call db.remove_appointment
    """
    pass


def list_customer_appointments():
    """
    Endpoint that returns appointments for a specific customer
    Get customer ID from customer and call db.view_appointments_for_customer
    """
    pass


def favorite_listing():
    """
    Endpoint to let a customer favorite a specific listing
    Should ideally only need a title, it's your choice how to implement it
    """
    pass


def unfavorite_listing():
    """
    Endpoint to let a customer unfavorite a specific listing
    Should ideally only need a title, but it's your choice how to implement it
    """
    pass


# # Update single listing
# @app.route('/listing/<int:id>', methods=['PUT'])
# def update_listing_route(id):
#     data = request.get_json()

#     selected_listing = view_listing_by_id(id)
#     new_listing = format_listing(selected_listing)
#     return jsonify(new_listing), 200


# category routes:

# Create a category
@app.route('/category', methods=['POST'])
def create_category_route():
    data = request.get_json()
    name = data['name']
    create_category(name)
    return jsonify({'message': "created listing successfully"}), 201


# app.run(debug=True) default way
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # bättre sätt
