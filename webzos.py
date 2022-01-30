import smartpy as sp


class Webzos(sp.Contract):
    def __init__(self):
        webzos = sp.utils.bytes_of_string(r'''
<!DOCTYPE html>
<html lang=en>
<head>
<meta charset=utf-8>
<title></title>
</head>
<body>
Your website here
</body>
</html>
''')
        self.init(webzos)


if 'templates' not in __name__:
    @sp.add_test('Webzos')
    def test():
        s = sp.test_scenario()
        s += Webzos()
