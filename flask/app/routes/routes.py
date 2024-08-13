from flask import Blueprint,request,jsonify
import requests
routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/api1/endpoint1', methods=['GET'])
def api1_endpoint1():
    return jsonify({"message": "Hello from API 1 - Endpoint 1"})

@routes_bp.route('/api2/endpoint2', methods=['GET'])
def api2_endpoint1():
    response = requests.get('http://127.0.0.1:8000/api1/endpoint1')
    data = response.json()
    return jsonify({"message": "Hello from API 2 - Endpoint 1", "api1_response": data})

@routes_bp.route('/api3/endpoint3', methods=['GET'])
def api3_endpoint1():
    return jsonify({"message": "Hello from API 3 - Endpoint 1"})


