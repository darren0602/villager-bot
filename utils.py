import constants
import psutil

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

        if args == []:
            print ("[I] Command {} has no arguments".format(command))
        elif len(args) > constants.MAX_ARGS:
            print("[W] Argument length exceeded! Using only first {}".format(constants.MAX_ARGS))
            args = temp[1:constants.MAX_ARGS + 1]

        return command, args
    else:
        return None, None

"""
Utility function to check if
a certain process is up on the
host machine.
"""
def check_if_process_running(proc_name):
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if proc_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False