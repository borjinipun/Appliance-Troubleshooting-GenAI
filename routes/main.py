from flask import Blueprint, render_template, request, jsonify
from services.ai_service import diagnose_problem_with_ai
from models.appliance import Appliance

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Home page."""
    return render_template('index.html')

@main_bp.route('/diagnose', methods=['POST'])
def diagnose():
    """Handles the diagnosis request."""
    try:
        data = request.get_json()
        problem_description = data.get('problem_description', '')
        appliance_category = data.get('appliance_category', '')

        if not problem_description or not appliance_category:
            return jsonify({'error': 'Both problem_description and appliance_category are required.'}), 400

        result = diagnose_problem_with_ai(problem_description, appliance_category)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@main_bp.route('/appliances')
def get_appliances():
    """Returns a list of supported appliances."""
    appliances = [
        Appliance("Refrigerator", "Refrigerator"),
        Appliance("Washer", "Washer"),
        Appliance("Dryer", "Dryer"),
        Appliance("Dishwasher", "Dishwasher"),
        Appliance("Oven", "Oven"),
        Appliance("Stove", "Stove"),
        Appliance("Microwave", "Microwave"),
    ]
    return jsonify([a.__dict__ for a in appliances])
