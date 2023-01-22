from library_python.commands import BaseCommand


class Command(BaseCommand):
    name: str = "Hello World"
    description: str = "Prints Hello World"

    def run(self):
        print("Hello World, Its Working")
