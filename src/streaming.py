#streaming.py

import re
import json
from collections import OrderedDict
from read_funcs import befriend, unfriend, purchase
from read_batch import initialize_network,run_meanstd
from calculate import find_friends, find_meanstd

#initialize list of users, social network, and purchase list
users = set()
friendlist = {}
purchases = {}
mean={}
std={}

#temporary file assignment
batch_file = 'log_input/batch_log.json'
stream_file = 'log_input/stream_log.json'
output_file = 'log_output/flagged_purchases.json'

#initialize the social network and purchase list with the batch file
init_vars=initialize_network(users,friendlist,purchases,batch_file)
for i in users:
    run_meanstd(i,friendlist,purchases,mean,std,init_vars)

#load streaming file and initialize output file
stream=open(stream_file,'r')
flagged=open(output_file,'w')
flagged.close()

#loads data from stream file line by line, updates database, and flags anomalies
for line in stream:
    data = json.loads(line)

    if data["event_type"]=="befriend" :
        befriend(data["id1"],data["id2"], users, friendlist, purchases)
    elif data["event_type"]=="unfriend" :
        unfriend(data["id1"],data["id2"], friendlist, purchases,users)
    elif data["event_type"]=="purchase" :
        user=int(data["id"])
        amount=float(data["amount"])
        if user in users:
            run_meanstd(user,friendlist,purchases,mean,std,init_vars)
            if amount > (3*std[user]+mean[user]) and mean[user] != 0:
                    flagged=open(output_file,'a')
                    temp_mean="%.2f" % mean[user]
                    temp_std="%.2f" % std[user]
                    f_purch=OrderedDict([("event_type",data["event_type"]),("timestamp",data["timestamp"]),("id",data["id"]),("amount",data["amount"]),("mean",temp_mean),("sd",temp_std)])
                    json.dump(f_purch,flagged,sort_keys=False)
                    flagged.write('\n')
                    flagged.close()
        purchase(data["id"],data["timestamp"],data["amount"], users, purchases,init_vars[1],friendlist)
        
stream.close()
