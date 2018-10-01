import numpy as np
from LIDARFilterClass import LIDARFilter

class medianFilter(LIDARFilter):
    
    def __init__(self, LIDARFilter, D):
        self.rangeN = LIDARFilter.rangeN
        self.rangeDist = LIDARFilter.rangeDist
        self.numSavedScans = D
        self.savedScans = []
        self.scansProcessed = -1
    
    def update( self, inArray ):
        
        npArrayAsInput = True
        if type(inArray) is list:
            numpyArray = np.array( inArray ) 
            npArrayAsInput = False
        else:
            numpyArray = inArray
        
        if len(numpyArray) < self.rangeN[0] or len(numpyArray) > self.rangeN[1]:
            print "scan length falls outside accepted range"
            return -1
        
        self.scansProcessed += 1
        numpyArrayI = np.append(numpyArray,[self.scansProcessed])
        
        if self.scansProcessed == 0:
            self.savedScans = numpyArrayI
            return inArray
        else:
            self.savedScans = np.vstack([self.savedScans,numpyArrayI])
    
        median = np.array([])
        
        for i in range(self.savedScans.shape[1]-1):
            self.savedScans = self.savedScans[self.savedScans[:,i].argsort()]
            if self.savedScans.shape[0] % 2 == 0:
                midValAindex = self.savedScans.shape[0]/2
                midValBindex = (self.savedScans.shape[0]/2)-1
                midValA = self.savedScans[midValAindex,i]
                midValB = self.savedScans[midValBindex,i]
                colMedian = ( midValA + midValB ) / 2.0
            else:
                colMedian = self.savedScans[self.savedScans.shape[0]/2,i]
            median = np.append(median,[colMedian])
        
        self.savedScans = self.savedScans[self.savedScans[:,self.savedScans.shape[1]-1].argsort()]
        
        if self.savedScans.shape[0] > self.numSavedScans:
            self.savedScans = np.delete(self.savedScans,(0),axis=0)
        
        if npArrayAsInput == True:
            return median
        else:
            return median.tolist()