DEFAULT_FINAL_GRAVITY = 1.014  # Somewhat arbitrary final gravity many beers are at
DEFAULT_EMPTY_WEIGHT = 17      # tare weight in lbs
WEIGHT_OF_WATER = 8.345        # lbs/gallon
OUNCES_PER_GALLON = 128        # ounces in a gallon
OUNCES_IN_PINT = 16

class Keg(object):
    ''' Represents a keg, by weight and the FG of liquid in it. Given a current
    weight, empty weight and FG we can determine how how much beer is in the keg.

    # Example usage:
    keg1 = Keg(empty_weight=17, final_gravity=1.008)
    keg1.setWeight(32)
    keg1.ounces   # => 183
    keg1.pints    # => 17
    keg1.gallons  # => 1.5
    Note: Numbers above aren't real, just for demo
    '''

    def __init__(self, final_gravity=DEFAULT_FINAL_GRAVITY, empty_weight=DEFAULT_EMPTY_WEIGHT):
        self.final_gravity = final_gravity
        self.empty_weight = empty_weight
        self.current_weight = None

    def _lbsToOz(self):
        ''' Given the number of pounds a keg is, compute the number of ounces of
        beer given the tare weight of the empty keg and the additional weight of the
        beer due to residual sugar.

        # http://www.brewangels.com/Beerformation/Weight.html
        # Light Lager with a FG of 1.008: 8.345 x 1.008 = 8.422 lb/g (round to 8.4)
        # Barley Wine with a FG of 1.030: 8.345 x 1.030 = 8.595 lb/g (round to 8.6)
        '''
        weight_of_liquid_in_keg = self.current_weight - self.empty_weight    # lbs
        beer_weight = WEIGHT_OF_WATER * self.final_gravity   # lbs/gallon
        gallons_of_beer = weight_of_liquid_in_keg / beer_weight
        return int(gallons_of_beer * OUNCES_PER_GALLON)

    def set_weight(self, lbs):
        self.current_weight = lbs

    @property
    def ounces(self):
        return int(self._lbsToOz())

    @property
    def pints(self):
        return int(self._lbsToOz() / OUNCES_IN_PINT)

    @property
    def gallons(self):
        return self._lbsToOz() / OUNCES_PER_GALLON
