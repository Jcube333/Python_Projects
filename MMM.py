lst1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean=sum(lst1)/len(lst1) 
lst1.sort()

if len(lst1)%2: #odd
   median=lst1[len(lst1)/2]
else:
   median=(lst1[int(len(lst1)/2)]+lst1[int(len(lst1)/2)-1])/2

modeCt =0 

for i in lst1:
    x=lst1.count(i)   
    if modeCt<x:
        modeCt=x
        mode=i

print("Mean of data is : " + str(mean))

print("Median of data is : " + str(median))

print("Mode of data is : " + str(mode))