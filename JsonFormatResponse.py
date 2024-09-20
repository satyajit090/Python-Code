from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask App'


@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello, {name}'

@app.route('/json')
def get_json():
    data = {
        'name':'Flask',
        'message':'demo json response',
        'success': True
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)