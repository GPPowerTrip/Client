#!/usr/bin/env python

import options
import help
import sys

ops = {
    'knight_ls':        ['get', 'knight/list'],
    'task_run':         ['post', 'task'],
    'task_ls':          ['get', 'task/list'],
    'task_check':       ['get', 'task/{param}/check'],
    'task_output':      ['get', 'task/{param}/output'],
    'task_rm':          ['delete', 'task/{param}'],
    'plugin_install':   ['post', 'plugin'],
    'plugin_ls':        ['get', 'plugin/list'],
    'plugin_rm':        ['delete', 'plugin/{param}'],
    'plugin_help':      ['get', 'plugin/{param}/help']
}

try:
    if len(sys.argv) < 4:
        if len(sys.argv) > 2 and sys.argv[2] in ops.keys():
            getattr(help, sys.argv[2])
        else:
            help.help()
    else:
        if sys.argv[3] in ops.keys():
            context = {
                'host': sys.argv[1],
                'port': sys.argv[2],
                'command': sys.argv[3],
                'method': ops[sys.argv[3]][0],
                'endpoint': ops[sys.argv[3]][1],
                'args': sys.argv[4:],
                'json': None,
                'data': '',
                'param': '',
                'headers': ''
            }
            print(getattr(options, sys.argv[3])(context))
        else:
            print("Invalid Command\n")
            help.help()
except:
    print("Closing...\n")

