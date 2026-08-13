from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

PIN = "2793"
balance = 10000

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    if data['pin'] == PIN:
        return jsonify({"success": True})

    return jsonify({"success": False})


@app.route('/balance')
def get_balance():
    global balance
    return jsonify({"balance": balance})


@app.route('/deposit', methods=['POST'])
def deposit():
    global balance

    amount = int(request.json['amount'])
    balance += amount

    return jsonify({"balance": balance})


@app.route('/withdraw', methods=['POST'])
def withdraw():
    global balance

    amount = int(request.json['amount'])

    if amount > balance:
        return jsonify({"success": False})

    balance -= amount

    return jsonify({
        "success": True,
        "balance": balance
    })


@app.route('/change_pin', methods=['POST'])
def change_pin():
    global PIN

    new_pin = request.json['pin']
    PIN = new_pin

    return jsonify({"success": True})


if __name__ == '__main__':
    app.run(debug=True)