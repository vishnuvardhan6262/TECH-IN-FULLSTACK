n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()
print()
n=5
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
print()
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()
n=5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()
n=6
c=65
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or n+1-i==j:
            print(chr(c),end=" ")
            c+=1
        else:
            print(" ",end=" ")
    print()

