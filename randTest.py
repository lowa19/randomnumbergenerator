import random, string, numpy as np, matplotlib.pyplot as plt, time

###################################
#createData makes a list of tuples
#a letter with a random number
#Parameters: ints for lowerbound and
#upperbounds for random numbers
#return: does not return anything
###################################
def createData(lowerBound, upperBound):
    alphabet = list(string.ascii_lowercase) #list of all letters in alphabet
    prob = [.0025,.0075,.0125,.02,.0275,.0325,.04,.045,.05,.0575,.0625,.0675,.075,.075,
            .0675,.0625,.0575,.05,.045,.04,.0325,.0275,.02,.0125,.0075,.0025]
    #prob is list of likelihoods for each letter, a-z for discrete distribution
    #randData = [(alphabet[np.random.choice(range(26), 1, p = prob)[0]]) for i in range(lowerBound, upperBound)] 
    #randData cycles through user's input and generates a random letter each time using prob
    randData = [(range(26)[np.random.choice(range(26), 1, p = prob)[0]]) for i in range(lowerBound, upperBound)]
    plt.hist(randData, bins=range(26))
    plt.show
    
    createFile(randData)
    return
  
def createFile(myList):
    with open("data.csv", "w") as myFile:
        myFile.write('\n'.join('%s' % tupl for tupl in myList))
    return



start_time = time.time()
createData(1,1000000)
print("%s seconds" % (time.time()-start_time))
