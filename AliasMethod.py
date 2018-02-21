import os
import random
import re
import sys
from decimal import *
from optparse import OptionParser
import matplotlib.pyplot as plt


class VoseAlias(object):
    """ A probability distribution for discrete weighted random variables and its probability/alias
    tables for efficient sampling via Vose's Alias Method (a good explanation of which can be found at
    http://www.keithschwarz.com/darts-dice-coins/).
    """

    def __init__(self, dist, size):
        """ (VoseAlias, dict) -> NoneType """
        sumOfInputs =0
        for i in dist.keys():
            sumOfInputs = sumOfInputs + dist[i]
            print(sumOfInputs)
            if dist[i] < 0:
                print("Error, no non-negative values.")
                return
        if abs(1 - sumOfInputs) > 0.05:
            print(sumOfInputs)
            print("Probabilities must add up to one.")
            return
        self.dist = dist
        self.alias_initialisation()
        self.sample_n(size)

    def alias_initialisation(self):
        """ Construct probability and alias tables for the distribution. """
        # Initialize variables
        n = len(self.dist)
        self.table_prob = {}   # probability table
        self.table_alias = {}  # alias table
        scaled_prob = {}       # scaled probabilities
        small = []             # stack for probabilities smaller that 1
        large = []             # stack for probabilities greater than or equal to 1

        # Construct and sort the scaled probabilities into their appropriate stacks
        for o, p in self.dist.items():
            scaled_prob[o] = Decimal(p) * n	#make new list of scaled probabilities (prob times n)

            if scaled_prob[o] < 1:	#put scaled values into new lists based on size
                small.append(o)	#values less than 1
            else:
                large.append(o)	#values greater than 1

        # Construct the probability and alias tables
        while small and large:	#while both lists are not empty
            s = small.pop()	#s is scaled probability less than 1
            L = large.pop()	#l is scaled probability greater than 1

            self.table_prob[s] = scaled_prob[s]	#put s in list of probabilities
            self.table_alias[s] = L	#put L in list of aliases corresponding to s

<<<<<<< HEAD
            scaled_prob[l] = (scaled_prob[l] + scaled_prob[s]) - Decimal(1) #Decimal of one 
=======
            scaled_prob[L] = (scaled_prob[L] + scaled_prob[s]) - Decimal(1)	#add s to L and subtract 1 to get new L (represents 1-s being taken from L)
>>>>>>> 27652009d06301afefb1772de955f1931b9f5928

            if scaled_prob[L] < 1:	#add new L to appropriate
                small.append(L)	#new L is less than 1
            else:
                large.append(L)	#new L is still greater than 1

        # The remaining outcomes (of one stack) must have probability 1
<<<<<<< HEAD
        while large:
            self.table_prob[large.pop()] = Decimal(1) # decimal of one

        while small:
            self.table_prob[small.pop()] = Decimal(1) #decimal of one
=======
        while large:	#small list is now empty but large list is not
            self.table_prob[large.pop()] = Decimal(1)	#round whatever values are left to 1

        while small:
            self.table_prob[small.pop()] = Decimal(1)	#round whatever values are left to 1
>>>>>>> 27652009d06301afefb1772de955f1931b9f5928

    def alias_generation(self):
        """ Return a random outcome from the distribution. """
        # Determine which column of table_prob to inspect
        col = random.choice(list(self.table_prob))

        # Determine which outcome to pick in that column
        if self.table_prob[col] >= random.uniform(0,1):
            return col
        else:
            return self.table_alias[col]

    def sample_n(self, size):
        """ Retrun a sample of size n from the distribution, and print the results to stdout. """
        # Ensure a non-negative integer as been specified
        n = int(size)
        try:
            if n <= 0:
                raise ValueError("Please enter a non-negative integer for the number of samples desired: %d" % n)
        except ValueError as ve:
            sys.exit("\nError: %s" % ve)



    def make_histogram(self, values, size):
        """ Prints off a histogram of the values created in alias_generation """

		
		

