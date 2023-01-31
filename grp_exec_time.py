from time import time 
lst=[[1,2,3],[4,5,6],[7,8,9]]
ans=[]
t=0
startTime=time()

for i in lst:
    k=0
    for j in i :
        if t==0:
            ans.append([j])

        else:
              
            ans[k].append(j)
            k+=1

    t=1

print(ans)        

endTime=time()
print(f'{endTime-startTime:.20f}')