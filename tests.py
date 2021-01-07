import constants
import defaults

def setup_test():
    result = True
    errors = 0
    warnings = 0

    try:
        constants.TOKEN
    except AttributeError:
        print("[E] Required key TOKEN not found!")
        errors += 1
        result = False

    try:
        if type(constants.MAX_ARGS) != int:
            print("[E] Key MAX_ARGS is not of type int!")
            errors += 1
            result = False
    except AttributeError:
        print("[W] Key MAX_ARGS not found! Using default value of {}".format(
            defaults.MAX_ARGS
        ))
        warnings += 1

    try:
        if type(constants.WHOIS_CHOICES) != list:
            print("[E] Key WHOIS_CHOICES is not of type list!")
            result = False
            errors += 1
    except AttributeError:
        print("[W] Key WHOIS_CHOICES not found! Using default value of {}".format(
            defaults.WHOIS_CHOICES
        ))
        warnings += 1

    print("Tests finished with {} errors and {} warnings".format(
        errors,
        warnings
    ))
    return result