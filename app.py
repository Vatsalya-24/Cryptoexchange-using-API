from flask import Flask, render_template, request
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

app = Flask(__name__)

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'd202b9b7-a677-4944-8463-837ba4453858',
}

session = Session()
session.headers.update(headers)

def get_price(symbol):
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        cleaned_data = data['data']  # Accessing the 'data' part of the JSON response

        # Find the item with the given symbol
        found_item = None
        for item in cleaned_data:
            if item['symbol'] == symbol:
                found_item = item
                break

        if found_item:
            return found_item['quote']['USD']['price']
        else:
            return None

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return None

def print_supported_symbols(cleaned_data):
    symbols = [item['symbol'] for item in cleaned_data]
    return symbols

@app.route('/')
def index():
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        cleaned_data = data['data']  # Accessing the 'data' part of the JSON response

        supported_symbols = print_supported_symbols(cleaned_data)
        return render_template('index.html', supported_symbols=supported_symbols)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return render_template('error.html')

@app.route('/exchange', methods=['POST'])
def exchange():
    from_symbol = request.form['from_symbol'].upper()
    to_symbol = request.form['to_symbol'].upper()
    amount_to_exchange = float(request.form['amount'])

    from_price = get_price(from_symbol)
    to_price = get_price(to_symbol)

    if from_price is not None and to_price is not None:
        amount_in_to_symbol = amount_to_exchange * (from_price / to_price)
        result = f"{amount_to_exchange} {from_symbol} is equal to {amount_in_to_symbol} {to_symbol}"
    else:
        result = "Symbol not found or there was an issue fetching data."

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
