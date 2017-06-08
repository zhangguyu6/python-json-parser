from myjson.dumps import tojson
from myjson.parser import Parse
from myjson.tokens import token


def dumps(pyobj):
    return tojson(pyobj)


def loads(json):
    return Parse(token(json)).parse_value()

__all__ = ["dumps", "loads"]
