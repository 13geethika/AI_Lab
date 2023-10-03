n=int(input("enter the disks"))
a=[i for i in range(1,n+1)]
b=[]
c=[]
def display(n,from_rod,to_rod):
        if from_rod=='A' and to_rod=='B':
            b.append(n);
            a.remove(n);
        elif from_rod=='B' and to_rod=='C':
            c.append(n);
            b.remove(n);
        elif from_rod=='A' and to_rod=='C':
            c.append(n);
            a.remove(n);
        elif from_rod=='B' and to_rod=='A':
            a.append(n);
            b.remove(n);
        elif from_rod=='C' and to_rod=='B':
            b.append(n);
            c.remove(n);
        elif from_rod=='C' and to_rod=='A':
            a.append(n);
            c.remove(n);
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        display(1,from_rod,to_rod);
        print('A:',a,'B:',b,'C:',c);
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    display(n,from_rod,to_rod)
    print('A:',a,'B:',b,'C:',c);
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
    #n =int(input("enter the no.of disks"))

TowerOfHanoi(n, 'A', 'C', 'B')