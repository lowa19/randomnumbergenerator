#import voseRunner

def calcProbs(vals):
    totalCount = 0
    probs = vals
    
    for i in vals.keys():
        totalCount = totalCount + vals[i]
        
    for i in vals.keys():
        probs[i] = (vals[i]/totalCount)


    return probs
