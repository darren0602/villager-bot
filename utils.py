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
        command = temp[0]
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
    else:
        return None, None
