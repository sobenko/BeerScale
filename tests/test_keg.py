import unittest
from beerscale.keg import Keg

class TestKeg(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        k = Keg(final_gravity=1.008, empty_weight=25)
        self.assertEquals(1.008, k.final_gravity)
        self.assertEquals(25, k.empty_weight)
        self.assertEquals(None, k.current_weight)

        # test defaults
        k = Keg()
        self.assertEquals(1.014, k.final_gravity)
        self.assertEquals(17, k.empty_weight)

    def test_set_weight(self):
        k = Keg()
        k.set_weight(20)
        self.assertEquals(20, k.current_weight)

    def test_ounces_to_lbs(self):
        # Create a keg with a gravity of water and no tare weight
        k = Keg(final_gravity=1.000, empty_weight=0)
        k.set_weight(8.345)   # 1 gallon of water
        self.assertEquals(128, k._lbsToOz())

        # More advanced, keg weight and other stuff
        k = Keg(final_gravity=1.015, empty_weight=10)
        k.set_weight(35)
        self.assertEquals(377, int(k._lbsToOz()))

    def test_ounces(self):
        k = Keg(final_gravity=1.000, empty_weight=0)
        k.set_weight(8.345)
        self.assertEquals(128, k.ounces)

    def test_pints(self):
        k = Keg(final_gravity=1.000, empty_weight=0)
        k.set_weight(8.345)
        self.assertEquals(8, k.pints)

    def test_gallons(self):
        k = Keg(final_gravity=1.000, empty_weight=0)
        k.set_weight(8.345)
        self.assertEquals(1, k.gallons)
