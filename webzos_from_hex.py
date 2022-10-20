import smartpy as sp


class Webzos(sp.Contract):
    def __init__(self):
        html_hex = 'HEX DUMP STARTING WITH 0x'
        self.init(sp.bytes(html_hex.strip()))


if 'templates' not in __name__:
    @sp.add_test('Webzos')
    def test():
        s = sp.test_scenario()
        s += Webzos()
