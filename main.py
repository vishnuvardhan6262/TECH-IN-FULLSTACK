""""
a=int(input("Enter a Number :"))
b=int(input("Enter another Number:"))
if a>b:
    print(f"{a} is Greater than B")
else:
    print(f"{b} is Greater thsn A")

x=int(input("Enter a Number :"))
y=int(input("Enter another Number:"))
sum=0
count=0
for i in range(x,y+1):
    if i%2==0:
        sum=sum+i
        count=count+1
print(sum/count)

def fun(year):
    return ((year%4==0 and year%100 !=0) or (year%400==0))
a=fun(int(input("Enter a Year :")))
if a==True:
    print("Its a Leap Year")
else:
    print("Not a Leap year")

num=int(input("Enter any number"))
if num==0 or num==1:
    print("Its not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("Its not a prime number")
            break
    else:
        print("Its a prime number")

a=123
def fun():
    a=10
    b=2.4
    c="sai"
print(fun.__code__.co_nlocals)
print(a)
"""

num=int(input("Enter any number:"))
sum=0
for i in range(num):
    number=int(input("Enter a Number:"))
    sum=sum+number
    a=(sum/num)
print(a)













