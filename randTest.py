import random, string, numpy as np, matplotlib.pyplot as plt, time

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
    showOccurances(randData, alphabet) #if we want to see the amount of each variable generated
    return



start_time = time.time()
createData(1,1000000)
print("%s seconds" % (time.time()-start_time))

###################################################################
## showOccurances gives a count of each variable in a list of data
## Parameters: listdata - our randomly generated data
##             alph - the list of variables
###################################################################
def showOccurances( listdata, alph ):
    dataList = [(i, listdata.count(i)) for i in alph]
    print(dataList)
    return
