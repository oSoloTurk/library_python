from library_python import commands


def test_help_command():
    """
    Test the help command
    """
    command = commands.HelpCommand()
    command.run()
