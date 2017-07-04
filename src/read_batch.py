#read-test.py

#Dependencies
import re
import json
from read_funcs import befriend, unfriend, purchase
from calculate import find_friends, find_meanstd

#intialize the social network and purchases
def initialize_network(users, friendlist, purchases, filename):
    
    #Open batch log file and initialize values of D and T, then strip header
    f = open(filename,'r')
    
    data=json.loads(f.readline())

    args=[int(data["D"]),int(data["T"])]
    
    for line in f:
        data = json.loads(line)
        if data["event_type"]=="befriend" :
            befriend(data["id1"],data["id2"], users, friendlist, purchases)
        elif data["event_type"]=="unfriend" :
            unfriend(data["id1"],data["id2"], friendlist, purchases, users)
        elif data["event_type"]=="purchase" :
            purchase(data["id"],data["timestamp"],data["amount"], users, purchases,args[1], friendlist)
            
    f.close()
    return args

#generates set of friends to required depth set in the batch_log file, then gives mean and std
def run_meanstd(user,friendlist,purchases,mean,std,init_vars):
    list_friends=find_friends(user,friendlist,init_vars[0])
    meanstd=find_meanstd(list_friends,purchases,init_vars[1])
    mean[user]=meanstd[0]
    std[user]=meanstd[1]
    return