#print("\n")
#print("\tGame Start\nNow the task is to move all of them to right side of the river")
#print("rules:\n1. The boat can carry at most two people\n2. If cannibals num greater than missionaries then the cannibals would eat the missionaries\n3. The boat cannot cross the river by itself with no people on board")

def check(m,c):
    if m!=c:
        print("Missionaries and cannibels must be in same number hence wrong input ")
        return
m=int(input("enter no.of missionaries "))
c=int(input("enter no.of cannibels "))
check(m,c)
lM = m          
lC = c           
rM=0            
rC=0             
userM = 0        
userC = 0        
k = 0
#print("\nM M M C C C |     --- | \n")
try:
    while(True):
        while(True):
            print("Left side -> right side river travel")
            #uM = user input for number of missionaries for left to right travel 
            #uC = user input for  number of cannibals for left to right travel 
            uM = int(input("Enter number of Missionaries travel => "))    
            uC = int(input("Enter number of Cannibals travel => "))
  
            if((uM==0)and(uC==0)):
                print("Empty travel not possible")
                print("Re-enter : ")
            elif(((uM+uC) <= m-1)and((lM-uM)>=0)and((lC-uC)>=0)):
                break
            else:
                print("Wrong input re-enter : ")
        lM = (lM-uM)
        lC = (lC-uC)
        rM += uM
        rC += uC
  
        print("\n")
        for i in range(0,lM):
            print("M ",end="")
        for i in range(0,lC):
            print("C ",end="")
        print("| --> | ",end="")
        for i in range(0,rM):
            print("M ",end="")
        for i in range(0,rC):
            print("C ",end="")
        print("\n")
  
        k +=1
  
        if(((lC==c)and (lM == m-1))or((lC==c)and(lM==m-1))or((lC==c-1)and(lM==m-2))or((rC==c)and (rM == m-1))or((rC==c)and(rM==m-1))or((rC==c-1)and(rM==m-2))):
            print("Cannibals eat missionaries:\nYou lost the game")
  
            break
  
        if((rM+rC) == m+c):
            print("You won the game : \n\tCongrats")
            print("Total attempt")
            print(k)
            break
        while(True):
            print("Right side -> Left side river travel")
            userM = int(input("Enter number of Missionaries travel => "))
            userC = int(input("Enter number of Cannibals travel => "))
              
            if((userM==0)and(userC==0)):
                    print("Empty travel not possible")
                    print("Re-enter : ")
            elif(((userM+userC) <= m-1)and((rM-userM)>=0)and((rC-userC)>=0)):
                break
            else:
                print("Wrong input re-enter : ")
        lM += userM 
        lC += userC
        rM -= userM
        rC -= userC
  
        k +=1
        print("\n")
        for i in range(0,lM):
            print("M ",end="")
        for i in range(0,lC):
            print("C ",end="")
        print("| <-- | ",end="")
        for i in range(0,rM):
            print("M ",end="")
        for i in range(0,rC):
            print("C ",end="")
        print("\n")
  
      
  
        if(((lC==c)and (lM == m-1))or((lC==c)and(lM==m-1))or((lC==c-1)and(lM==m-2))or((rC==c)and (rM == m-2))or((rC==c)and(rM==m-1))or((rC==c-1)and(rM==m-2))):
            print("Cannibals eat missionaries:\nYou lost the game")
            break
except EOFError as e:
    print("\nInvalid input please retry !!")