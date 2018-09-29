import numpy as np

class LIDARFilter:
    
    #Allowed variable ranges stored as tuple of form (min,max)
    rangeN = (200,1000)
    rangeDist = (0.03,50)
    
    #Each filter object should have an update method
    def update( self, numpyArray ):
        raise NotImplementedError()