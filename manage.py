import importlib
import sys
import os

arguments = sys.argv
module_name = os.path.dirname(os.path.abspath(__file__)).split("/")[-1]

if len(arguments) == 1:
    """
    If no arguments are passed to the script
    Work in setup mode"""
    arguments.append("help")

if module_name in sys.modules:
    """
    If the module is already imported by installed before
    Clean the module from the cache and use the local version
    """
    del sys.modules[module_name]
    print(f"{module_name} already installed, using local version")

module = importlib.import_module(module_name)
commands = module.commands

command_name = arguments.pop(1)

if command_name in ["-h", "--help", "help"]:
    command_name = "HelpCommand"

command: commands.BaseCommand = getattr(
    getattr(commands, command_name), "Command", None
)

if command is None:
    command = commands.HelpCommand

command = command()
command.main()
