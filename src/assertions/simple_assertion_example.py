"""
In code assertion statement consists of the following boiler code (it may change depending on what it does)
- assert keyword (asssert)
- a condition (university_open == 'open')
- a comma with a string to display when condition is false (,'sorry university is closed I am afraid')
"""

university_status = "open"

# Try logging the traceback
import traceback

try:
    # This one is true so we do not get any AssertionError
    assert university_status == "open", (
        "University is not open sorry. Try again on Monday."
    )
    # False, therefore we get an AssertionError
    assert university_status == "closed", (
        "University is not open sorry. Try again on Monday"
    )
except:
    error_file = open("assertion_error.txt", "w")
    error_file.write(traceback.format_exc())
    error_file.close()
    print(
        'assertion error was logged as "assertion_error.txt" in the directory where the program ran from'
    )
