x=[1,8,6,2,5,4,8,3,7]
# x=[1, 5, 4, 3]
# x=[3, 1, 2, 4, 5]
# x=[1,1]
l=[]
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            z=x[j]*(j-i)
            l.append(z)
        else:
            z=x[i]*(j-i)
            l.append(z)
print(max(l))

    


