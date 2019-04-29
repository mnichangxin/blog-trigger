import os, time

from flask import Blueprint, request, jsonify

from ...secure import verify_signature
from ...delivery import delivery

hooks = Blueprint('hooks', __name__)

@hooks.route('/payload', methods=['POST'])
def payload():
    res = {}
    headers = request.headers
    try:
        x_hub_signature = headers['X-Hub-Signature']
    except KeyError as e:
        res = {
            'status': 0,
            'msg': '请求无效'
        }
    else:
        body_data = request.data
        x_hub_event = headers['X-GitHub-Event']
        if verify_signature(x_hub_signature, body_data):
            res = {
                'status': 1,
                'msg': '成功',
                'data': {
                    'version': '1.0'
                }
            }
            if x_hub_event == 'ping':
                delivery(request.get_json())
        else:
            res = {
                'status': 0,
                'msg': '验证失败'
            }
    return jsonify(res)