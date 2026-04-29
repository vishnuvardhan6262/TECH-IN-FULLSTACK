n=int(input("Enter 1:"))
n1=int(input("Enter 2 :"))
for n in range(n,n1+1):
    t=n
    dc=0
    while n!=0:
        n=n//10
        dc+=1
    n=t
    s=0
    while n!=0:
        r=n%10
        s=s+r**dc
        n=n//10
    if s==t:
        print(t,end=" ")