import constants
import defaults

"""
Wrapper around split to split
message into command and list
of args.
"""
def msg_split(message, command_prefix="$"):
    if message.startswith(command_prefix):
        temp = message.split()

        command = temp[0].strip(command_prefix)
        args = temp[1:]

        try:
            MAX_ARGS = constants.MAX_ARGS
        except AttributeError:
            MAX_ARGS = defaults.MAX_ARGS

        if args == []:
            print ("[I] Command {} has no arguments".format(command))
        elif len(args) > MAX_ARGS:
            print("[W] Argument length exceeded! Using only first {}".format(MAX_ARGS))
            args = temp[1:MAX_ARGS + 1]

        return command, args

    return None, None

def is_valid_command(string, command, allow_uppercase=True,
                    alternative_commands=None):
    # Simplest case
    if string == "{}".format(command):
        return True

    # Uppercase
    if allow_uppercase:
        if string == "{}".format(command.upper()):
            return True

    if alternative_commands != None:
        if string in alternative_commands:
            return True

        # Uppercase alternatives
        uppercase_alternative_commands = [alternative_command.upper() for alternative_command in alternative_commands]
        if string in uppercase_alternative_commands:
            return True

    return False
