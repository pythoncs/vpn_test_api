#  -*-coding:utf8 -*-
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
import json
import pymongo

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
        # 存储至数据库
        client = pymongo.MongoClient(host='meta.houselai.com', port=20202)
        db = client.vpn_db
        db.authenticate('cuishu', 'cuishu123')
        p = db.user_info
        print(res['phone'])
        p.insert_many([res])
        # 获取数据
        object_id = p.find_one({'phone': res['phone']})['_id']
        print(type(object_id))

        response = {
            "status_code": "200",
            'object_id': str(object_id)
        }
        resp = make_response(response)
        # resp.set_cookie('gender', 'man')
        cookie = request.cookies.get('name')
        print('cookie:------>', cookie)

        return resp


api.add_resource(VpnModel, '/houselai')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6666, debug=True)
  
