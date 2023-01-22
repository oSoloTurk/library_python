import os
import sys
import importlib
from argparse import ArgumentParser

from library_python import structures


def get_commands() -> "BaseCommand":
    for name in os.listdir(commands_path):
        module_name = name.replace(".py", "")
        module = importlib.import_module(f"library_python.commands.{module_name}")
        command = getattr(module, "Command", None)
        if command is None:
            continue
        yield command


class BaseCommand(structures.GlobalDefinableObject):
    name: str
    description: str

    def add_arguments(self, parser: ArgumentParser) -> None:
        # This method is not necessary to implement
        pass

    def run(self, **options):
        raise NotImplementedError("Command must implement run() method")

    def get_parser(self):
        parser = ArgumentParser()
        self.add_arguments(parser)
        return parser

    def main(self):
        parser = self.get_parser()
        options = parser.parse_args()
        self.run(**vars(options))

    @classmethod
    def get_module(cls):
        return sys.modules[cls.__module__].__name__.split(".")[-1]


class HelpCommand(BaseCommand):
    name: str = "Help Command"
    description: str = "Shows all available commands"

    def run(self, **options):
        print(">> Available commands:")
        command: BaseCommand

        for command in get_commands():
            command_instance = command()
            print(
                f" - {command_instance.name}\n"
                f"\t{command_instance.description}\n\n"
                f"{command_instance.get_parser().print_help()}\n"
                f"{'-' * 20}"
            )


commands = []
print("> Loading Commands...")
commands_path = str(os.path.join(os.path.dirname(__file__)))
for command in get_commands():
    commands.append(command)

__all__ = ["BaseCommand", "HelpCommand"] + commands
