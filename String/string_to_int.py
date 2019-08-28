import string
import functools
def string_to_int(s):
    return functools.reduce(lambda sum,c : sum * 10 + string.digits.index(c),s[s[0] == '-':],0) * (-1 if s[0] == '-' else 1)

