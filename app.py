from flask import Flask, jsonify, request
from database import create_listing

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_todos():
    return jsonify({'message': "welcome to hemnet!"})


@app.route('/listing', methods=['GET'])
def get_listing():
    data = request.get_json()
    return jsonify(create_listing(data['name'], data['price'], data['description'], data['category_id'], data['broker_id']))

# Create a listing


@app.route('/listing', methods=['POST'])
def create_listing_route():
    data = request.get_json()
    name = data['name']
    price = data['price']
    description = data['description']
    category_id = data['category_id']
    broker_id = data['broker_id']
    create_listing(name, price, description, category_id, broker_id)
    return jsonify({'message': "created listing successfully"})


# app.run(debug=True) default way
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # bättre sätt


# url = "postgresql://postgres:Vanligt123!@localhost/carappdb"
# conn = psycopg2.connect(url)

# '''If everything works fine you will get a
# message that Flask is working on the first
# page of the application
# '''


# @app.route('/')
# def check():
#     return 'Flask is working'


# @app.route('/connect')
# def index():
#     with conn:
#         conn = psycopg2.connect(
#             "postgresql://postgres:root@localhost:5432/postgres")
#         return 'it works'
