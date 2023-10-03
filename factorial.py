n=int(input("enter a number "))
s=1
if n==0 or n==1:
    print(1)
else:
    for i in range(1,n+1):
        s=s*i
print("Factorial of "+str(n)+" is "+str(s))