from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined conversion rates
conversion_rates = {
    'USD': 1.00,  # Example rate: 1 USD = 1 USD
    'EUR': 0.91,  # Example rate: 1 USD = 0.85 EUR
    'CAD': 1.38,  # Example rate: 1 USD = 1.38 CAD
    'JPY': 144.18  # Example rate: 1 USD = 110.0 JPY
    # Add more currencies and their rates as needed
    # Rates defined from simple google search
}


@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.get_json()

    if not data or 'amounts' not in data or 'currency' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    amounts = data['amounts']
    currency = data['currency']

    if currency not in conversion_rates:
        return jsonify({'error': 'Unsupported currency'}), 400

    rate = conversion_rates[currency]
    converted_amounts = [amount * rate for amount in amounts]

    return jsonify({
        'convertedAmounts': converted_amounts
    })


if __name__ == '__main__':
    app.run(port=3001, debug=True)
