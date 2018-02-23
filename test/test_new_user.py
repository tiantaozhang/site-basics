import json
from unittest import TestCase


class TestNew_user(TestCase):
    def test_new_user(self):
        add1 = ['1']
        add2 = ['2','3',{'1':'4'}]
        add = add1
        add += add2
        a = [{'id': 1}, {'id': 2}, {"id": 3}]
        a.pop(1)
        a.insert(0,{'id':2})
        print(a)

        result = [{'idfa': 'ABC-BCD','clientType':10},{'idfa':'BCD-EDF','clientType':10}]
        body = "".join(json.dumps(result).split())
        print(body)
        print(type(body))

        fza = frozenset('a')
        print(fza)
        adict = {fza: 1, 'b': 2}
        print(adict[fza])

        import shelve
        f = shelve.open('1.txt')
        print(f.get('egg'))
        f.close()

        from urllib import urlopen

        webpage = urlopen('http://www.python.org')
        import re
        text = webpage.read()
        m = re.search('<a href="([^"]+)".*?>about</a>', text, re.IGNORECASE)
        print(m.group(0), m.group(1))
