import jwt
from jwt import DecodeError


def create_token(data, secret):
    return jwt.encode(data, secret)


def verify_signature(token):
    try:
        msg = jwt.decode(token, key='acelera', verify=True, algorithms='HS256')
        return msg
    except DecodeError:
        return {"error": 2}