#read_funcs.py

#adds friends to each corresponding friendlist upon action
def befriend(arg1, arg2, users, friendlist, purchases):
    user1 = int(arg1)
    user2 = int(arg2)

    if users.intersection((user1,)) == set():
        users.add(user1)
        purchases[user1]=[]
    if users.intersection((user2,)) == set():
        users.add(user2)
        purchases[user2]=[]
        
    if user1 in friendlist:
        temp = friendlist[user1]
        temp.add(user2)
        friendlist[user1]=temp
    else:
        temp=set([user1,user2])
        friendlist[user1]=temp
        
    if user2 in friendlist:
        temp = friendlist[user2]
        temp.add(user1)
        friendlist[user2]=temp
    else:
        temp=set([user2,user1])
        friendlist[user2]=temp    
    return

#unfriends the specified users (assuming they are already friends)
def unfriend(arg1, arg2, friendlist, purchases,users):
    user1=int(arg1)
    user2=int(arg2)
    if user1 in friendlist and user2 in friendlist:
        temp1 = friendlist[user1]
        temp2 = friendlist[user2]
        temp1.remove(user2)
        temp2.remove(user1)
        friendlist[user1]=temp1
        friendlist[user2]=temp2
    else:
        if user2 not in users:
            users.add(user2)
            friendlist[user2]=set([user2])
            purchases[user2]=[]
        if user1 not in users:
            users.add(user1)
            friendlist[user1]=set([user1])
            purchases[user1]=[]
    
    return

#logs purchase for user and truncates purchase list to length of history
def purchase(arg1, timeofpurch, arg2, users, purchases, hist_length, friendlist):
    user = int(arg1)
    purchase = float(arg2)

    if users.intersection((user,)) == set():
        users.add(user)
        friendlist[user]=set([user])
    
    if user in purchases:
        temp = purchases[user]
        if len(temp) >= hist_length:
            temp=temp[1:]
        temp.append([timeofpurch, purchase])
        purchases[user]=temp
    else:
        purchases[user] = [[timeofpurch, purchase],]

    return