from flask import Flask, request, jsonify, render_template
from iban_checker import iban_is_valid

app = Flask(__name__)


@app.route('/validate-iban/', methods=['POST'])
def validate_iban():
    """ recieves a call from a web-server to validate an IBAN """
    data = request.json
    iban = data.get("iban")

    if iban == None:
        return jsonify(statusCode=400, message="IBAN number must be included")

    valid = iban_is_valid(iban)  #Accesses the function for Iban validation from iban-checker.py
    print(valid)   
    return jsonify(statusCode=200, valid=valid)
