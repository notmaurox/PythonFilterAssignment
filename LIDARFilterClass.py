import numpy as np

class LIDARFilter:
    #Parent class of other filters that deal with LIDAR Data. 
    #Defines rule that each subclass must have an implemented update method.
    #Has helper method for checking if length of an input is within set range
    
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