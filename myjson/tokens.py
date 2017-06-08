"""
token json to list
"""


class WrongGrammarError(Exception):
    "json error"


def token(stream):
    i = 0
    tokens = []
    while i < len(stream):
        word = stream[i]
        if word == "{":
            tokens.append(('BEGIN_OBJECT', word))
            i += 1
        elif word == "}":
            tokens.append(('END_OBJECT', word))
            i += 1
        elif word == "[":
            tokens.append(('BEGIN_ARRAY', word))
            i += 1
        elif word == "]":
            tokens.append(('END_ARRAY', word))
            i += 1
        elif word == ":":
            tokens.append(('COLON', word))
            i += 1
        elif word == ",":
            tokens.append(('COMMA', word))
            i += 1
        elif word == "\"":
            start = i
            i += 1
            while stream[i] != "\"":
                i += 1
                if i > len(stream):
                    raise WrongGrammarError
            tokens.append(('STRING', stream[start + 1:i]))
            i += 1
        elif word == "t":
            i += 4
            tokens.append(('BOOlEAN', True))
        elif word == "f":
            i += 4
            tokens.append(('BOOlEAN', False))
        elif word == "n":
            i += 4
            tokens.append(('NULL', None))
        elif word in "1234567890":
            start = i
            i += 1
            while stream[i] in "1234567890.eE":
                i += 1
                if i > len(stream):
                    raise WrongGrammarError
            tokens.append((convertnum(stream[start:i])))
        else:
            i += 1
    return tokens


def convertnum(numstr):
    if ('.' or 'e' or 'E') in numstr:
        floatnum = float(numstr)
        return "FLOAT", floatnum
    else:
        return "INT", int(numstr)
