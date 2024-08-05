# CS-362-Microservice-A
Currency converter microservice and test program

## Prerequisites ##

Ensure you have Python and Flask installed. You can install Flask and the required dependencies using pip

pip install Flask flask-cors requests

## Running the Microservice ##

Save the provided microservice code to a file named currency_converter.py.

Run the microservice
The microservice will start and listen for requests on http://localhost:3001.

## Microservice Endpoint ##
URL: http://localhost:3001/convert
Method: POST
Content-Type: application/json

## Request Format ##
To programmatically request data from the microservice, you can use Python's requests library.
The microservice expects a JSON object with the following format

```
{
  "amounts": [price1, price2, price3, ...],
  "currency": "EUR"
}
```

## Response Format ##
The response from the microservice will be a JSON object containing the converted amounts.
The microservice responds with a JSON object containing the converted amounts
```
{
  "convertedAmounts": [converted_price1, converted_price2, converted_price3, ...]
}
```

## UML Sequence Diagram ##
![image](https://github.com/user-attachments/assets/5e31d889-e3e0-48ab-b346-25388b10230c)
