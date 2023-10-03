l=[0,1]
n=int(input("how many numbers you want in fibonacci series "))
for i in range(0,n-2):
    l.append(l[i]+l[i+1])
print(l)