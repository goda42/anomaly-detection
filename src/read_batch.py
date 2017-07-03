#read-test.py

#Dependencies
import re
from read_funcs import befriend, unfriend, purchase

#Open batch log file and initialize values of D and T, then strip header
f = open('log_input/batch_log.json','r')

batch = f.readlines()
f.close()

d=int(re.match(".*D\":\"(.)\"",batch[0]).group(1))
t=int(re.match(".*T\":\"(.*)\"",batch[0]).group(1))


batch = batch[1:]
batch.sort()
#print(batch)

#initialize list of users
users = set()
friendlist = {}
purchases = {}

for i in batch:
    r=re.match(".*\"(.*)\".*\"(.*)\".*\"(.*)\".*\"(.*)\".*\"(.*)\".*\"(.*)\".*\"(.*)\".*\"(.*)\"",i)
    if r.group(2)=="befriend" :
        befriend(r.group(6),r.group(8), users, friendlist)
    elif r.group(2)=="unfriend" :
        unfriend(r.group(6),r.group(8), friendlist)
    elif r.group(2)=="purchase" :
        purchase(r.group(6),r.group(4),r.group(8), users, purchases)

print(users)
print(friendlist)
print(purchases)
