from flask import Flask, request, jsonify, render_template
from iban_checker import iban_is_valid

app = Flask(__name__)


@app.route('/validate-iban', methods=['POST'])
def validate_iban():
    """  """
    data = request.json
    iban = data.get("iban")

    if iban == None:
        return jsonify(statusCode=400, message="IBAN number must be included")

    valid = iban_is_valid(iban)
    print(valid)   
    return jsonify(statusCode=200, valid=valid)
