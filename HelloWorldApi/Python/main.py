import flask
from flask import request, jsonify

app = flask.Flask(__name__)

message = {
    'messsage': "Hello, world!"
}

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)