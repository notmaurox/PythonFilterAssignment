import numpy as np

class LIDARFilter:
    
    def __init__ (self, minRangeN, maxRangeN, minRangeDist, maxRangeDist):
        self.rangeN = (minRangeN,maxRangeN)
        self.rangeDist = (minRangeDist,maxRangeDist)
        
    #Each filter object should have an update method
    def update( self, numpyArray ):
        raise NotImplementedError()