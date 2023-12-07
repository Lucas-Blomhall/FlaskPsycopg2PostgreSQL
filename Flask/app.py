from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_todos():
    return jsonify({'todos': "hej world"})


if __name__ == '__main__':
    # app.run(debug=True) default way
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
