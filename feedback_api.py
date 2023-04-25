from flask import Flask, request, jsonify
from main import generate_modified_code

app = Flask(__name__)

@app.route('/modify-code', methods=['POST'])
def modify_code():
    code = request.json.get('code', '')
    modified_code = generate_modified_code(code)
    return jsonify({"modified_code": modified_code})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
