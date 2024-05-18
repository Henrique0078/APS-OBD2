from flask import Blueprint, jsonify
import os
import json

metrics_blueprint = Blueprint('metrics', __name__)

@metrics_blueprint.route('/')
def metrics():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    metrics_path = os.path.join(current_dir, 'metrics.json')  
    with open(metrics_path, 'r') as f:
        data = json.load(f)
    return jsonify(data)