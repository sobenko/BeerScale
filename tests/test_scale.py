import unittest
from beerscale.scale import Scale

class TestScale(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        ''' stupidly verify constructor '''
        s = Scale(low_read=0, low_weight=0, high_read=500, high_weight=50)
        self.assertEquals(0, s.low_read)
        self.assertEquals(0, s.low_weight)
        self.assertEquals(500, s.high_read)
        self.assertEquals(50, s.high_weight)

    def test_weight(self):
        ''' Verify our interpolation works as expected '''
        s = Scale(low_read=0, low_weight=0, high_read=500, high_weight=50)
        self.assertEquals(25, s.weight(analog_read=250))
        self.assertEquals(40.5, s.weight(analog_read=405))

        # Out of upper bounds
        self.assertEquals(60, s.weight(analog_read=600))

        # Below lower bounds
        self.assertEquals(-10, s.weight(analog_read=-100))
