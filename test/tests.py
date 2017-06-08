import unittest
import json
from myjson import loads, dumps

pyobj = {"a": 1, "b": 1.0, "c": [1, 2, 3], "d": {
    "a": 1}, "e": None, "f": True, "g": False, "h": {"a": [1, 2, 3, {"b": 1}]}}
Json = json.dumps(pyobj)


class Common(unittest.TestCase):
    def test_load(self):
        self.assertEqual(pyobj, loads(Json))

    def test_dumps(self):
        self.assertEqual(Json, dumps(pyobj))

if __name__ == '__main__':
    unittest.main()
