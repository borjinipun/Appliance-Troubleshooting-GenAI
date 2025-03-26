import random
from utils.helpers import get_appliance_categories

def diagnose_problem_with_ai(problem_description, appliance_category):
    """
    Simulates AI-powered diagnosis using a Generative AI model.
    REPLACE THIS WITH ACTUAL GEN-AI INTEGRATION (e.g., Vertex AI, OpenAI).
    """
    if appliance_category.lower() not in get_appliance_categories():
        return {
            "diagnosis": "Appliance category not supported.",
            "solutions": ["Provide a valid appliance category (e.g., refrigerator, washer, dryer, etc.)."],
        }

    placeholder_responses = {
        "refrigerator": [
            "The issue might be related to the compressor. Check for unusual noises.",
            "It could be a problem with the defrost system. Is there ice buildup?",
            "The temperature sensor could be malfunctioning.",
        ],
        "washer": [
            "The washer may not be draining correctly. Check the drain hose.",
            "The spin cycle might be affected by a worn belt.",
            "There could be an issue with the water pump.",
        ],
        "dryer": [
            "The dryer might not be heating up. Check the heating element.",
            "The drum may not be turning. Check the belt.",
            "There could be a problem with the airflow. Check the vent.",
        ],
        "dishwasher": [
            "The dishwasher may not be draining. Check the drain hose and filter.",
            "The dishes may not be getting clean. Check the spray arms.",
            "The dishwasher may not be filling with water. Check the water inlet valve.",
        ],
        "oven": [
            "The oven is not heating to the correct temperature. Check the temperature sensor.",
            "The oven is not heating at all. Check the heating element (electric) or igniter (gas).",
            "The self-cleaning function is not working. This could be a control board issue.",
        ],
        "stove": [
            "The burner is not lighting (gas). Check the igniter.",
            "The burner is not heating (electric). Check the heating element.",
            "The control knob is not working. The knob or the switch may need replacing.",
        ],
        "microwave": [
            "The microwave is not heating. This could be a magnetron problem.",
            "The turntable is not spinning. Check the turntable motor.",
            "The microwave is sparking. Stop use immediately and check the waveguide cover.",
        ],
    }

    response = random.choice(placeholder_responses[appliance_category.lower()])
    
    return {
        "diagnosis": f"Gen-AI suggests: {response}",
        "solutions": [
            "Consult a repair manual.",
            "Check online resources.",
            "Contact a qualified technician.",
        ],
    }
