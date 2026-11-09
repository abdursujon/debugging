import logging
from practice_logging.valid_email_log import numUniqueEmails


def main():
    logging.basicConfig(
        filename="/home/sujon/Project/debugging/logs/valid_email.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    # calls the function from valid_email
    numUniqueEmails(
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ]
    )
    numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"])
    numUniqueEmails([])


if __name__ == "__main__":
    main()
