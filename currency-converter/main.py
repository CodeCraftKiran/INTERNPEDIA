from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

apikey = os.environ.get('APIKEY')
url = "https://api.freecurrencyapi.com/v1/latest"
response = requests.get(f"{url}?apikey={apikey}")
data = response.json()['data']
data_keys = list(data.keys())


def currency_convertor(base_code, target_code, source_amount):
    base_code_price = data[base_code]
    target_code_price = data[target_code]
    target_amount = (source_amount / base_code_price) * target_code_price
    target_amount = round(target_amount, 2)
    print(target_amount)
    return target_amount


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        base_code = request.form.get('base')
        target_code = request.form.get('target')
        try:
            base_amount = float(request.form.get('base_amount'))
        except ValueError:
            return render_template('index.html', data=data_keys, message=True)
        else:
            print(base_amount, base_code, target_code)
            target_amount = currency_convertor(base_code, target_code, base_amount)
            return render_template('index.html',
                                   data=data_keys,
                                   target_amount=target_amount,
                                   base_amount=base_amount,
                                   target_code=target_code,
                                   base_code=base_code)
    return render_template('index.html', data=data_keys)


if __name__ == '__main__':
    app.run(debug=True)