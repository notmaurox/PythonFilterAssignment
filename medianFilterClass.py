import numpy as np
from LIDARFilterClass import LIDARFilter

class medianFilter(LIDARFilter):
    
    def __init__(self, LIDARFilter, D):
        self.rangeN = LIDARFilter.rangeN
        self.rangeDist = LIDARFilter.rangeDist
        self.numSavedScans = D
        self.savedScans = [[]]
        self.scansProcessed = -1
        self.scanLength = -1
    
    def update( self, inArray ):
        # Handles preservation of list or numpy array type
        npArrayAsInput = True
        if type(inArray) is list:
            numpyArray = np.array( inArray ) 
            npArrayAsInput = False
        else:
            numpyArray = inArray
        #Checks length of input array
        if not LIDARFilter.goodLength(self,inArray) or \
                 (len(inArray) != self.scanLength and self.scansProcessed > -1):
            print "length of inArray outside accepted range"
            return -1
        #Updates input array with counter and tracks scans processed
        self.scansProcessed += 1
        numpyArrayI = np.append(numpyArray,[self.scansProcessed])
        
        #Caase that this is first input scan
        if self.scansProcessed == 0:
            self.savedScans = numpyArrayI
            self.scanLength = len(inArray)
            return inArray
        else:
            #Case that this is not the first input scan
            self.savedScans = np.vstack([self.savedScans,numpyArrayI])
    
        #Array used for building median of currently saved input arrays
        median = np.array([])
        
        #loop through each element across each each input array.
        #Skip last element as that is a placeholder for order preservation. 
        for i in range(self.savedScans.shape[1]-1):
            self.savedScans = self.savedScans[self.savedScans[:,i].argsort()]
            #Case that the median is the average of two elements in middle of 
            #sorted list
            if self.savedScans.shape[0] % 2 == 0:
                midValAindex = self.savedScans.shape[0]/2
                midValBindex = (self.savedScans.shape[0]/2)-1
                midValA = self.savedScans[midValAindex,i]
                midValB = self.savedScans[midValBindex,i]
                colMedian = ( midValA + midValB ) / 2.0
            else:
                #Case that median is the center element in sorted list
                colMedian = self.savedScans[self.savedScans.shape[0]/2,i]
            #Add middle value to growing median vector. 
            median = np.append(median,[colMedian])
        #Re-order arrays by the order in which they were recieved with newest last
        self.savedScans = self.savedScans[self.savedScans[:,self.savedScans.shape[1]-1].argsort()]
        #If enough previous arrays already saved, remove the oldest one. 
        if self.savedScans.shape[0] > self.numSavedScans:
            self.savedScans = np.delete(self.savedScans,(0),axis=0)
        
        #Return a numpy array if input was numpy array, else return list
        if npArrayAsInput == True:
            return median
        else:
            return median.tolist()