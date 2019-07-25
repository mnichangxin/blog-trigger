import hmac, hashlib

def verify_signature(x_hub_signature, body_data):
    key = b'abcdefg' or ''
    h = hmac.new(key, digestmod=hashlib.sha1)
    h.update(body_data)
    local_signature = h.hexdigest()

    print(local_signature)

    return 'sha1={}'.format(local_signature) == x_hub_signature