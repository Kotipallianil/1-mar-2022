x=[1,2,1,3,2,4,2,5,4,6,5,7,6,4]
list=[]
list1=[]
for i in x:
	if i%2==1:
		if i not in list:
			list.append(i)
			list1.append(x.count(i))
print(list)
print(list1)
