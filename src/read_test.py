#read-test.py

#Dependencies
import re

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
batch_dict={}
batch_dict[
for i in batch:
    r=re.match(".*\"(.*)\".*\"(.*)\".*\"(.*)\".*\"(.*)\".*\"(.*)\".*\"(.*)\".*\"(.*)\".*\"(.*)\"",i)
    new_record = {r.group(1) : r.group(2), r.group(3) : r.group(4), r.group(5) : r.group(6), r.group(7) : r.group(8)
    batch_dict.update(new_record)

print(batch_dict)
