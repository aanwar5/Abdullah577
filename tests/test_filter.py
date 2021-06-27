#tests/test_filter.py

from Abdullah577 import lib

abc = 'Dani'
cde = 'Sarah'

def test_hello_le_wagon():
    assert type(lib.hello_le_wagon(abc)) != int
    assert len(lib.hello_le_wagon(cde)) != 0