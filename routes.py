from flask import Blueprint, jsonify
import time

main = Blueprint('main', __name__)
start = time.perf_counter()


@main.route("/")
def hello():
    '''Returns Hello World & HTTP 200 Status Code'''
    return "Hello World", 200


@main.route("/status/alive")
def status_alive():
    '''Returns an empty body & HTTP 200 Status Code'''
    return "", 200


@main.route("/status/ready")
def status_ready():
    '''Returns 500 IFF app has been up for less than 10 seconds'''
    end = time.perf_counter()
    if (end - start) < 10:
        return jsonify({"ready": "false"}), 500
    else:
        return jsonify({"ready": "true"}), 200


@main.route('/<path:path>')
def catch_all(path):
    '''Returns Catch all return for invalid paths'''
    return f'{path} page does not exist', 404
