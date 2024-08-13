from flask import Blueprint,request,jsonify
routes_bp = Blueprint('routes', __name__)

@routes_bp.route("/")
def Home():
    return "This is Home page"

