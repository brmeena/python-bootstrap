import sys
import traceback

sys.path.append("../")
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def checkIfValidEmail(email):
    if (re.fullmatch(regex, email)):
        return True
    return False