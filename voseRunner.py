from AliasMethod import VoseAlias
import time

#initialize time
start_time = time.time()

#set values and weights for generation
dist = {"A" : .1, "B" : .2, "C" : .3, "D" : .1, "E" : .3}


#make an instance of VoseAlias using data from dist and number of values
VA = VoseAlias(dist, 1000)

#print out the time elapsed
print("%s seconds" % (time.time()-start_time))
