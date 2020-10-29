def check_email(string):
    return ' ' not in string and '@' in string and (string.find('@') < string.rfind('.') - 1)
