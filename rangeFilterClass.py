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
            
        if len(numpyArray) < self.rangeN[0] or len(numpyArray) > self.rangeN[1]:
            print "scan length falls outside accepted range"
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