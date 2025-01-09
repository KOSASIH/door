# utils/validators.py

import re

def validate_email(email):
    """
    Validate the email format.
    
    :param email: Email address to validate.
    :return: True if valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_username(username):
    """
    Validate the username format.
    
    :param username: Username to validate.
    :return: True if valid, False otherwise.
    """
    return len(username) >= 3 and len(username) <= 20 and username.isalnum()
