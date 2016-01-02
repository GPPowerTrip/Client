#!/usr/bin/env python

import requests
import json


class Rest:
    @staticmethod
    def get(host, port, endpoint, param=''):
        print("here")
        r = requests.get('http://' + host + ':' + port + '/' + endpoint + '/' + param, timeout=3)
        if r.status_code != 200: print('ERROR: ' + r.text); raise ValueError('Problem connecting')
        return json.loads(r.text)

    @staticmethod
    def delete(host, port, endpoint, param=''):
        r = requests.delete('http://' + host + ':' + port + '/' + endpoint + '/' + param, timeout=3)
        if r.status_code != 200: print('ERROR: ' + r.text); raise ValueError('Problem connecting')
        return json.loads(r.text)

    @staticmethod
    def post(host, port, endpoint, param='', data=None, json=None, **kwargs):
        r = requests.post('http://' + host + ':' + port + '/' + endpoint + '/' + param, data=data, json=json, timeout=5, **kwargs)
        if r.status_code != 200: print('ERROR: ' + r.text); raise ValueError('Problem connecting')
        return r.text
