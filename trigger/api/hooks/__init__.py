import os, time
from concurrent.futures import ThreadPoolExecutor
from flask import Blueprint, request, jsonify

from ...secure import verify_signature

hooks = Blueprint('hooks', __name__)

def exec_sh():
    time.sleep(10)
    print(os.popen('cd / && ls').readlines())

@hooks.route('/payload', methods=['POST'])
def payload():
    res = {}
    try:
        x_hub_signature = request.headers['X-Hub-Signature']
    except KeyError as e:
        res = {'status': 0}
    else:
        body_data = request.data
        if verify_signature(x_hub_signature, body_data):
            # executor = ThreadPoolExecutor(1)
            # executor.submit(exec_sh)
            res = {
                'status': 1,
                'data': {
                    'version': '1.0'
                }
            }
        else:
            res = {
                'status': 0
            }
    return jsonify(res)