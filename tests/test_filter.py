#tests/test_filter.py

from Abdullah577 import simpleimage 
from Abdullah577.lib import main, sepia_pixel

def test_main():
    assert(main()) !=0
    assert(sepia_pixel(50)) != int