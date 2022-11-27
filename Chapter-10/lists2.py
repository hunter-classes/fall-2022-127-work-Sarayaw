#4
def average (numlist):
    total= 0
    for num in numlist:
        total +=num
        
    return total/ len(numlist)


#6

import random
sm=[]
for i in range (3):
    sm.append(random.randint (0,50))
    
def sum_ofsquares(sm):
    sum_ofsquares=0
    for i in (sm):
        squared=i*i
        sum_ofsquares += squares
    return sum_ofsquares

print(sum_ofsquares(sm))
