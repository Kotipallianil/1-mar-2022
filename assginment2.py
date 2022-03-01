x=[1,1,2,8,3,2,3,4,0,5,7,6,8,9,9]
list=[]
for i in x:
    if i not in list:
        if x.count(i)==1:
            list.append(i)
print(list)
