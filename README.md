```
help:
    ('Usage: excalibot help COMMAND')
    ('General application usage: excalibot HOST PORT COMMAND PARAMETERS')
    ('COMMAND:')
    ('  help            #  this information')
    ('  knight_ls       # List available bots')
    ('  task_run        # Schedule new attacks')
    ('  task_ls         # List running tasks')
    ('  task_check      # Check task completion status')
    ('  task_output     #  completed task output')
    ('  task_rm         # Clear task from control center')
    ('  plugin_install  # Install new plugin')
    ('  plugin_ls       # List installed plugins')
    ('  plugin_rm       # Clear installed plugin')
    ('  plugin_help     # Get help for installed plugin')


knight_ls:
    ('List available bots')
    ('Usage: excalibot HOST PORT knight_ls SINCE')
    ('SINCE: (optional)')
    ('  Show only bots alive in the last SINCE seconds')


task_run:
    ('Schedule new tasks')
    ('Usage: excalibot HOST PORT task_run ATTACK KEY:VALUE')
    ('ATTACK:')
    ('  installed plugin name')
    ('KEY:VALUE: (optional)')
    ('  list of parameters to the attack, in a key:value format')


task_ls:
    (' list of ongoing tasks')
    ('Usage: excalibot HOST PORT task_ls')


task_check:
    ('Check task completion status')
    ('Usage: excalibot HOST PORT task_check ID block')
    ('ID:')
    ('  id of the task to get status')
    ('block: (optional)')
    ('  block until task is completed')


task_output:
    (' task output')
    ('Usage: excalibot HOST PORT task_output ID')
    ('ID:')
    ('  id of the task to get output')


task_rm:
    ('Clear task from control center')
    ('Usage: excalibot HOST PORT task_rm ID')
    ('ID:')
    ('  id of the task to deleted')


plugin_install:
    ('Install new plugin')
    ('Usage: excalibot HOST PORT plugin_install URL')
    ('URL:')
    ('  url to the plugin resource')


plugin_ls:
    (' list of available plugins')
    ('Usage: excalibot HOST PORT plugin_ls')


plugin_rm:
    ('Clear plugin from control center')
    ('Usage: excalibot HOST PORT task_rm NAME')
    ('NAME:')
    ('  name of the plugin to deleted')


plugin_help:
    ('Get help for installed plugin')
    ('Usage: excalibot HOST PORT plugin_help NAME')
    ('NAME:')
    ('  name of the plugin to get help')
```
