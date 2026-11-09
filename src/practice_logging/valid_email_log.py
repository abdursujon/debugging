import logging 

# __name__ is "email", so this is getLogger("email")
logger = logging.getLogger(__name__)


def numUniqueEmails(emails:list[str]) -> list[str]:
    logger.info('Unique and valid email list requested for emails=%s', emails )
    if len(emails) == 0:
        logger.warning('No emails provided in emails=:%s', emails)

    local = [e.replace('.','').split('+')[0].split('@')[0] for e in emails]
    logger.debug('valid local name provided=%s', local)

    domain = [e.split('@')[1] for e in emails]
    logger.debug('valid domain provided=%s', domain)

    valid_email = set()
    for i in range(len(local)):
        valid = local[i] + '@' + domain[i]
        logger.debug('Current valid email address=%s', valid)
        valid_email.add(valid)
    
    valid_email = list(valid_email)
    logger.debug('return type=%s', type(valid_email))
    logger.debug('The function numUniqueEmails(emails) produced the valid email list=%s', valid_email)
    logger.debug('-'*60)
    return valid_email

    
