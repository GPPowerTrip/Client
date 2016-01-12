#!/usr/bin/env python
import time
import sys
import requests


def request(context):
    try:
        context['endpoint'] = context['endpoint'].replace("{param}", context['param'])
        r = getattr(requests, context['method'])(
                'http://' + context['host'] + ':' + context['port'] + '/' + context['endpoint'] + '/',
                data=context['data'], json=context['json'], timeout=5, headers=context['headers'])
        if r.status_code != 200: print('ERROR STATUS CODE: ' + r.text); raise ValueError('Problem connecting')
        return r.text
    except:
        print('Connection error');
        sys.exit(0)


def print_list(bot_list):
    properties = ['id', 'busy', 'ipAddress', 'lastSeen', 'os']
    response = "ID BUSY ADDRESS LASTSEEN OS\n"
    current = time.time()
    for bot in sorted(bot_list, key=lambda k: k['lastSeen'], reverse=True):
        bot['lastSeen'] = int((current - bot['lastSeen'] / 1000))
        for key in properties:
            if key in bot:
                response += '\'' + str(bot[key]) + "\' "
            elif key in bot['properties']:
                response += '\'' + str(bot['properties'][key]) + "\' "
            else:
                response += '\'\''
        response += "\n"
    return response


def bot_ls(bot_list):
    current = time.time()
    response = ''
    for bot in sorted(bot_list, key=lambda k: k['lastSeen'], reverse=True):
        bot['lastSeen'] = int((current - bot['lastSeen'] / 1000))
        for key in bot['properties']: bot[key] = bot['properties'][key]
        bot.pop('properties')
        response += str(bot) + '\n'
    return response


def parameter(context):
    if len(context['args']) == 0: return "Invalid parameters"
    if len(context['args']) > 0: context['param'] = context['args'][0]
    return request(context)


def hash_args(args):
    param = {}
    for element in args:
        if len(element.split(':')) < 2: return -1
        key = str(element.split(':')[0])
        value = str(':'.join(element.split(':')[1:]))
        param[key] = value
    return param
