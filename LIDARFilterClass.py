import numpy as np

class LIDARFilter:
    
    def __init__ (self, minRangeN, maxRangeN, minRangeDist, maxRangeDist):
        self.rangeN = (minRangeN,maxRangeN)
        self.rangeDist = (minRangeDist,maxRangeDist)
        
    #Each filter object should have an update method
    def update( self, inArray ):
        raise NotImplementedError("update method not implemented in class")
        
    def goodLength( self, inArray):
        if len(inArray) < self.rangeN[0] or len(inArray) > self.rangeN[1]:
            print "scan length falls outside accepted range"
            return False
        return True