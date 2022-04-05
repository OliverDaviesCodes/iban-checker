from flask import Flask, request, Response, render_template
from iban_checker import iban_is_valid


def create_app():
    app = Flask(__name__)

    @app.route('/validate-iban', methods=['POST'])
    def validate_iban():
        """ recieves a call from a web-server to validate an IBAN """
        data = request.json
        iban = data.get("iban")

        if iban == None:
            return Response("{'Message':'IBAN number must be included'}", status=400, mimetype='application/json')

        valid = iban_is_valid(iban)  #Accesses the function for Iban validation from iban-checker.py
        print(valid)   
        return Response('{"valid": "%s"}' % (valid), status=200, mimetype='application/json')

    return app