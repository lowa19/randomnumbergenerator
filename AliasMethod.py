import os, random, re, sys, time
from decimal import *
from optparse import OptionParser
import matplotlib.pyplot as plt


class VoseAlias(object):
    """ A probability distribution for discrete weighted random variables and its probability/alias
    tables for efficient sampling via Vose's Alias Method 
    """
	
    start_time = time.time()
    init_time = 0
    generation_time = 0
    generation_and_print_time = 0
    total_time = 0

######################################################################################################

    def __init__(self, dist, size):
        """ (VoseAlias, dict) -> NoneType """
        sum_of_inputs = 0
        for i in dist.keys():
            sum_of_inputs = sum_of_inputs + dist[i]
            if dist[i] < 0:
                print("Error, no non-negative values.")
                return
        if abs(1 - sum_of_inputs) > 0.05:
            print("Probabilities must add up to one.")
            return
        self.dist = dist
        self.alias_initialisation()
        self.init_time = time.time() - self.start_time
        self.sample_n(size)

########################################################################################################		
		
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

            scaled_prob[L] = (scaled_prob[L] + scaled_prob[s]) - Decimal(1)	#add s to L and subtract 1 to get new L (represents 1-s being taken from L)

            if scaled_prob[L] < 1:	#add new L to appropriate
                small.append(L)	#new L is less than 1
            else:
                large.append(L)	#new L is still greater than 1

        # The remaining outcomes (of one stack) must have probability 1
        while large:	#small list is now empty but large list is not
            self.table_prob[large.pop()] = Decimal(1)	#round whatever values are left to 1

        while small:
            self.table_prob[small.pop()] = Decimal(1)	#round whatever values are left to 1

###################################################################################################
			
    def alias_generation(self):
        """ Return a random outcome from the distribution. """
        # Determine which column of table_prob to inspect
        col = random.choice(list(self.table_prob))

        # Determine which outcome to pick in that column
        if self.table_prob[col] >= random.uniform(0,1):
            return col
        else:
            return self.table_alias[col]
			
######################################################################################################

    def sample_n(self, size):
        """ Retrun a sample of size n from the distribution, and print the results to stdout. """
        # Ensure a non-negative integer as been specified
        n = int(size)
        try:
            if n <= 0:
                raise ValueError("Please enter a non-negative integer for the number of samples desired: %d" % n)
        except ValueError as ve:
            sys.exit("\nError: %s" % ve)

        vals = []	#initialize empty list of values
        for i in range(n):	#loop through n times
            vals.append(self.alias_generation())	#get one alias_generation value (O(1)) and append (O(1)) it to vals
        self.generation_time = time.time() - self.init_time
        #print(vals)	#print the entire list
        self.count_data(self.dist, vals) #function to print data nicely
        self.generation_and_print_time = time.time() - self.generation_time
        self.make_histogram(vals, n)	#make a histogram of results
        self.print_times()

####################################################################################################		

    def make_histogram(self, values, size):
        """ Prints off a histogram of the values created in alias_generation """
        plt.hist(values, bins = "auto")	#values are the data being counted
        plt.title("Occurrences of Randomly Generated Values")	#title of histogram
        plt.xlabel("Value")	#x-axis label
        plt.ylabel("Count")	#y-axis label
        self.total_time = time.time() - self.start_time
        plt.show()	#print window of histogram

		
########################################################################################################

    def print_times(self):
        """This method just prints off the times taken for each part"""
        #print("\nInitialization time: %s seconds" %self.init_time)
        #print("\nGeneration time: %s seconds" %self.generation_time)
        print("\nPrint time: %s seconds" %self.generation_and_print_time)
        print("\nTotal time: %s seconds" %self.total_time)
########################################################################################################

    def count_data(self, dist, vals):
        """Makes the data nicer and easier to read"""
        for x in dist:
            varCount = vals.count(x)
            print("Count of " + x + ": " + str(varCount)) #print the count
            print("Percent: " + str(100*(varCount / len(vals))) + "%") #print the percent
		
		

