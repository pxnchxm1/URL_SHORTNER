from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)
app.config['BASE_URL'] = 'http://localhost:5000/'

url_mapping = {}

def generate_short_link():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(4))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    short_url = generate_short_link()
    url_mapping[short_url] = original_url
    return render_template('shortened.html', short_url=app.config['BASE_URL'] + short_url)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    original_url = url_mapping.get(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return render_template('not_found.html'), 404


