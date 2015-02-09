class Scale(object):
    ''' Represents a postal scale attached to an arduino. Using two known
    weights along with their analog reads, we can use linear interpolation to
    determine the weight on the scale.

    Example usage:

    scale1 = Scale(22.13, 0, 413.12, 55.0)
    scale1.weight(analog_read=143.5)   => 31
    '''
    def __init__(self, low_read, low_weight, high_read, high_weight):
        self.low_read = low_read
        self.high_read = high_read
        self.low_weight = low_weight
        self.high_weight = high_weight

    def weight(self, analog_read):
        ''' gets the current weight given an analog read using linear interpolation
        of previous low and high reads

        (y - y0) / (x - x0) = (y1 - y0) / (x1 - x0)
        y = y0 + (y1 - y0) * ((x - x0) / (x1 - x0)
        WHERE
        x0, y0 are the low read/weight pair
        x1, y1 are the highread/weight pair
        x, y are the current pair, solving for y (weight)
        '''
        lw = float(self.low_weight)
        hw = float(self.high_weight)
        lr = float(self.low_read)
        hr = float(self.high_read)

        weight = lw + (hw - lw) * ((analog_read - lr) / (hr - lr))

        return weight
