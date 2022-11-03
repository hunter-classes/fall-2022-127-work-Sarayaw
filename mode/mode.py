#1
list1=[18,16,35,220,999,2,48]

print("The biggest number is:", max (list1))



#2 11/03/2022
def fmode (dataset):
    n=100
    lists= [0] * n
    
    for item in dataset:
        lists[item] +=1
        
    numbers = lists[0]
    for num in lists:
        if num > numbers:
            numbers= lists.index(num)
            
    return numbers

data= [1,1,1,2,2,2,2,3,3,4,4,4,4,4]
print(fmode(data))
