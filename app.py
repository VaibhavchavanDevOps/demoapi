from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    # Extract data from the POST request
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid or missing JSON payload"}), 400

    # Retrieve the operands and operation
    operand1 = data.get("operand1")
    operand2 = data.get("operand2")
    operation = data.get("operation")

    if operand1 is None or operand2 is None or not operation:
        return jsonify({"error": "Missing required fields (operand1, operand2, operation)"}), 400

    try:
        operand1 = float(operand1)
        operand2 = float(operand2)
    except ValueError:
        return jsonify({"error": "Operands must be numbers"}), 400

    # Perform the requested operation
    result = None
    if operation == "add":
        result = operand1 + operand2
    elif operation == "subtract":
        result = operand1 - operand2
    elif operation == "multiply":
        result = operand1 * operand2
    elif operation == "divide":
        if operand2 == 0:
            return jsonify({"error": "Division by zero is not allowed"}), 400
        result = operand1 / operand2
    else:
        return jsonify({"error": f"Unsupported operation '{operation}'"}), 400

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
