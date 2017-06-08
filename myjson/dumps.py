"""
dump python object to json
"""


class NotImplementedJsonSeriError(NotImplementedError):
    "json convert NotImplemented"


def tojson(pyobject):
    if isinstance(pyobject, dict):
        return "{" + \
            ", ".join(["{}: {}".format(tojson(key), tojson(value)) for key, value in pyobject.items()]) + \
            "}"

    elif pyobject is None:
        return "null"

    elif pyobject is True:
        return "true"

    elif pyobject is False:
        return "false"

    elif isinstance(pyobject, list):
        return "[" + ", ".join([tojson(value) for value in pyobject]) + "]"

    elif isinstance(pyobject, str):
        return "\"" + pyobject + "\""

    elif isinstance(pyobject, int):
        return str(pyobject)

    elif isinstance(pyobject, float):
        return str(pyobject)

    else:
        raise NotImplementedJsonSeriError
