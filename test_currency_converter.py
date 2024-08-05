import requests
import json


url = 'http://localhost:3001/convert'


test_payloads = [
    {"amounts": [100, 200, 300], "currency": "EUR"},
    {"amounts": [100, 200, 300], "currency": "CAD"},
    {"amounts": [100, 200, 300], "currency": "JPY"}
]


headers = {'Content-Type': 'application/json'}


def test_payload(payload):
    # Print the payload being sent
    print(f"Sending request with payload: {payload}")

    # Make the POST request to the microservice
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        response_data = response.json()
        converted_amounts = response_data['convertedAmounts']
        print(f"Converted amounts for currency {payload['currency']}:")
        for amount, converted in zip(payload['amounts'], converted_amounts):
            print(f"  {amount} USD = {converted:.2f} {payload['currency']}")
        print()
    else:
        print("Failed to connect to the microservice:", response.status_code)
        print("Response:", response.text)


for payload in test_payloads:
    test_payload(payload)
