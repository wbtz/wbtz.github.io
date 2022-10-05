import smartpy as sp


class Webzos(sp.Contract):
    def __init__(self):
        html = r'''
<!DOCTYPEhtml>
<html lang=en>
<meta charset=utf8>
<title>WEBZOS</title>
<body>
CONTENT OF YOUR WEBSITE HERE
'''
        self.init(sp.utils.bytes_of_string(html.strip()))


if 'templates' not in __name__:
    @sp.add_test('Webzos')
    def test():
        s = sp.test_scenario()
        s += Webzos()
