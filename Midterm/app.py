from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/api/welcome', methods=['POST'])
def welcome():
    data = request.json
    name = data.get('name', 'Stranger')
    message = f'Welcome, {name}!'
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)
