# utils/helpers.py

import random
import string

def generate_random_string(length=10):
    """
    Generate a random string of fixed length.
    
    :param length: Length of the random string.
    :return: Randomly generated string.
    """
    letters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string
