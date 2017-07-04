#calculate.py
from math import sqrt

#generates friendlist to required depth
def find_friends(user,friendlist,links):
    user_list=friendlist[user]
    i=2
    while i <= links:
        for j in user_list.copy():
            user_list.update(friendlist[j])
        i+=1
    return user_list

#uses friendlist to calculate the mean and std over the required # of transactions
def find_meanstd(user_list,purchases,hist_length):
    temp=[]
    for i in user_list:
        if i in purchases:
            temp.append(purchases[i])
    current_purchases=[val for sublist in temp for val in sublist]
    current_purchases.sort()
    current_purchases.reverse()
    current_purchases=[val for sublist in current_purchases for val in sublist]    
    current_purchases=current_purchases[1::2]
    current_purchases=current_purchases[0:(hist_length-1)]

    if len(current_purchases) > 0:
        mean=sum(current_purchases)/len(current_purchases)
        std=sqrt(sum((a-mean)**2 for a in current_purchases)/len(current_purchases))
    else:
        mean=0
        std=0

    return [mean,std]