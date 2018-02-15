from AliasMethod import VoseAlias
import time

start_time = time.time()

dist = { "1" : 0.1, "2" : 0.2, "8" : 2, "9" : .5}

VA = VoseAlias( dist )

VA.sample_n( size = 10000 )

#print("%s seconds" % (time.time()-start_time))