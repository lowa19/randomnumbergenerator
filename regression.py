

def regEq(x):
    y = x+1
    return y

def reg(deltax, numBoxes):
    d = {0:regEq(0)}
    i = 1
    while i<numBoxes:
        d[i*deltax] = regEq(i*deltax)
        i+=1
    
    return d
