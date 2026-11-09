'''
Logging levels (highest → lowest):
CRITICAL (50) - a serious error, the program may not keep running
ERROR    (40) - a problem stopped part of the program from working
WARNING  (30) - something unexpected, but the program still works
INFO     (20) - confirmation that things are working normally
DEBUG    (10) - detailed info for diagnosing problems

logging.disable(level) turns off that level AND everything below it:
logging.disable(logging.CRITICAL)  -> disables everything
logging.disable(logging.ERROR)     -> only CRITICAL still shows
'''