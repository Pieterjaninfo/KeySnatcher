import re
from time import time
print('Program started...')

KEY_REGEX = '[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}'

# Unused regex
KEY_REGEX2 = '[a-zA-Z0-9]{15}'
KEY_REGEX3 = '[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}'
KEY_REGEX4 = '[a-zA-Z0-9]{25}'

reg = re.compile(KEY_REGEX)


def extract_code(msg):
    if reg.search(msg):
        return reg.findall(msg)
    return None


def extract_code_direct(msg):
    return reg.findall(msg)


if __name__ == '__main__':
    msg_1 = 'KEY:FN2HQ-H479X-TRZZV try out this one\t AECLK-XWIIK-VEE8C!GET EM GETM'
    msg_2 = 'THIS IS A WONDER FULLLLLLL AMAZING KEY GET IT WHILE ITS HOT MATES FN2HQ-H479X-TRZZV YW BOIS'
    msg_3 = 'LOOL YOU GOT FOOLED BOI XDDDDDD'
    msg_4 = '1234567890'
    msg_5 = '123456789012356780123456789012356780123456789012356780123456789012356780123456789012356780'
    msg_6 = '123456789012356780123456789012356780123456789012356780123456789012356780123456789012356780123456789012356780123456789012356780123456789012356780123456789012356780123456789012356780'
    #msg_4 = 10 chars, msg_5 = 100 chars, msg_6 = 200 chars

    x = extract_code(msg_1)
    if x:
        print(x)
    else:
        print('No match for:', msg_1)

    # Speed Testing
    loops = 2000000

    for message in [msg_4, msg_5, msg_6]:
        start = time()
        for i in range(0, loops):
            extract_code(message)
        print('extract_code(' + message + '):', time() - start, 's')

        start = time()
        for i in range(0, loops):
            extract_code_direct(message)
        print('extract_code_direct(' + message + '):', time() - start, 's')
