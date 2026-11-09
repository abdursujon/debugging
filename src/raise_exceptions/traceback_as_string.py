"""
Instead of crashing our program right when an exception occurs, we can write the traceback information to
a log file and keep our program running. This way we can look the log file later, wehn we are ready to debug
out code. Below is an example provided.
"""

import traceback

print(dir(traceback))


def bacon():
    raise Exception("This is the error message")


def spam():
    bacon()


try:
    spam()
except:
    error_file = open("traceback_error_info.txt", "w")
    error_file.write(traceback.format_exc())
    error_file.close()
    print('The traceback info was written to "error_info.txt" file')
