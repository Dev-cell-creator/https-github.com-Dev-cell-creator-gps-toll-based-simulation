from flask import Flask, render_template, request, jsonify
from vehicle_detection import detect_vehicles
from toll_calculation import calculate_toll
from payment_gateway import PaymentGateway

app = Flask(__name__)

# Route to render index.html
@app.route('/')
def index():
    return render_template('index.html')

# Example endpoint for vehicle detection (simulated)
@app.route('/detect_vehicle', methods=['POST'])
def detect_vehicle():
    # Simulate vehicle detection logic here if needed
    # Example: frame = request.files['frame'].read()
    # Simulated response for demonstration
    vehicles = [{'x': 100, 'y': 100, 'w': 50, 'h': 50}]  # Simulated vehicles coordinates
    return jsonify({'vehicles': vehicles})

# Endpoint to calculate toll
@app.route('/calculate_toll', methods=['POST'])
def calculate_toll_endpoint():
    data = request.json
    vehicle_type = data.get('vehicleType')
    distance = float(data.get('distance', 0))
    if vehicle_type and distance:
        toll = calculate_toll(vehicle_type, distance)
        return jsonify({'toll': toll})
    else:
        return jsonify({'error': 'Invalid request parameters'})

# Example endpoint for payment processing (simulated)
@app.route('/process_payment', methods=['POST'])
def process_payment():
    data = request.json
    user_id = data.get('user_id')
    amount = float(data.get('amount', 0))
    payment_gateway = PaymentGateway()
    success = payment_gateway.process_payment(user_id, amount)
    return jsonify({'success': success})

if __name__ == '__main__':
    app.run(debug=True)
