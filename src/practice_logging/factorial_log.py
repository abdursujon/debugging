import logging

# we can disable logging by just using one liner
# logging.disable(logging.CRITICAL)
logging.basicConfig(
    level=logging.DEBUG, format=("%(asctime)s - %(levelname)s - %(message)s")
)
logging.debug("Start of DEBUG")


def factorial(n):
    total = 1
    k = [
        2,
        3,
        4,
    ]
    logging.debug("Start of factorial(%s)" % (n))
    for i in range(1, n + 1):
        total = total * i
        logging.debug("i is " + str(i) + " total is " + str(total))
    logging.debug("End of factorial(%s)" % (n))
    logging.debug("Total is %s" % total)
    return total


factorial(5)
logging.debug("End of DEBUG")
