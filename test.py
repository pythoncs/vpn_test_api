#  -*-coding:utf8 -*-
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
import binascii
import hashlib

app = Flask(__name__)
api = Api(app)


class VpnModel(Resource):
    # 向前端传数据
    @app.route('/')
    def get(self):
        response = {
            "phone": "17601042712"
        }
        return response

    @app.route('/')
    def post(self):
        # 前端传来的用户数据
        res = request.json
        str_bin = res['valid_string'].encode('utf-8')

        hex_str = binascii.hexlify(str_bin)
        sign = hashlib.sha256(hex_str).hexdigest()
        print(sign)
        # hash_str = hashlib.sha256(str_bin).hexdigest().encode()
        # sign = binascii.hexlify(hash_str).decode('utf-8')

        response = {
            "status_code": "200",
            'sign': sign
        }

        return response


api.add_resource(VpnModel, '/sign')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
