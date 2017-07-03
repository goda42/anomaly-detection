def befriend(arg1, arg2, users, friendlist):
    user1 = int(arg1)
    user2 = int(arg2)

    if users.intersection((user1,)) == set():
        users.add(user1)
    if users.intersection((user2,)) == set():
        users.add(user2)
        
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

def unfriend(arg1, arg2, friendlist):
    user1=int(arg1)
    user2=int(arg2)
    temp1 = friendlist[user1]
    temp2 = friendlist[user2]
    temp1.remove(user2)
    temp2.remove(user1)
    friendlist[user1]=temp1
    friendlist[user2]=temp2
    
    return
    
def purchase(arg1, timeofpurch, arg2, users, purchases):
    user = int(arg1)
    purchase = float(arg2)

    if users.intersection((user,)) == set():
        users.add(user)
    
    if user in purchases:
        temp = purchases[user]
        temp.append([timeofpurch, purchase])
        purchases[user]=temp
    else:
        purchases[user] = [[timeofpurch, purchase],]

    return