from flask import Flask, render_template, request
import string
import secrets
import pyperclip

app = Flask(__name__)


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    # new_password = ''.join(secrets.choice(characters) for _ in range(length))
    new_password = ""
    for _ in range(length):
        new_password += secrets.choice(characters)
    return new_password


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        length = int(request.form.get('len_passwords'))
        generated_password = generate_password(length)
        pyperclip.copy(generated_password)
        return render_template('index.html', password=generated_password)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)