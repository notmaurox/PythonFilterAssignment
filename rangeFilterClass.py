import numpy as np
from LIDARFilterClass import LIDARFilter

class rangeFilter(LIDARFilter):
    
    def __init__(self,LIDARFilter):
        self.rangeN = LIDARFilter.rangeN
        self.rangeDist = LIDARFilter.rangeDist
        self.scansCorrected = 0
        self.updatesMade = 0
    
    def update(self, inArray ):
        
        npArrayAsInput = True
        if type(inArray) is list:
            numpyArray = np.array( inArray ) 
            npArrayAsInput = False
        else:
            numpyArray = inArray
            
        if not LIDARFilter.goodLength(self,inArray):
            print "length of inArray outside accepted range"
            return -1
        
        for value in np.nditer(numpyArray, op_flags=['readwrite']):
            if value < self.rangeDist[0]:
                value[...] = self.rangeDist[0]
                self.updatesMade += 1
            if value > self.rangeDist[1]:
                value[...] = self.rangeDist[1]
                self.updatesMade += 1
        self.scansCorrected += 1
        
        if npArrayAsInput == True:
            return numpyArray
        else:
            return numpyArray.tolist()