import numpy as np
from FilterClass import LIDARFilter

class medianFilter(LIDARFilter):
    
    def __init__(self, D):
        self.numSavedScans = D
        self.savedScans = []
        self.scansProcessed = -1
    
    def update( self, numpyArray ):
        
        self.scansProcessed += 1
        numpyArrayI = np.append(numpyArray,[self.scansProcessed])
        
        if self.scansProcessed == 0:
            self.savedScans = numpyArrayI
            return numpyArray
        else:
            self.savedScans = np.vstack([self.savedScans,numpyArrayI])
        
        median = []
        median = np.array(median)
        
        for i in range(self.savedScans.shape[1]-1):
            self.savedScans = self.savedScans[self.savedScans[:,i].argsort()]
            if self.savedScans.shape[0] % 2 == 0:
                midValAindex = self.savedScans.shape[0]/2
                midValBindex = (self.savedScans.shape[0]/2)-1
                midValA = self.savedScans[midValAindex,i]
                midValB = self.savedScans[midValBindex,i]
                colMedian = ( midValA + midValB ) / 2 
            else:
                colMedian = self.savedScans[self.savedScans.shape[0]/2,i]
            median = np.append(median,[colMedian])
        
        self.savedScans = self.savedScans[self.savedScans[:,self.savedScans.shape[1]-1].argsort()]
        
        if self.savedScans.shape[0] > self.numSavedScans:
            self.savedScans = np.delete(self.savedScans,(0),axis=0)
        
        return median
        
## Store scans in diectionary with key = N (length of scan). Add sequentially as a stack
## When update is called, use length of query to look up elements in diectionary