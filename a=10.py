"""
print('hello world')
a=int(input("enter the value of A>>>"))
b=int(input("enter the value of B>>>"))
c=a+b
print("sum of two numbers is ",c)

print("swaping!!")
a=a+b
b=a-b
a=a-b
print("a=",a,"b=",b)

d=int(input("enter kilometer for conversion "))
d=d*0.621371
print("converted value is ",d)

e=int(input("enter a number "))
if(e==0):
  {
    print("the number is zero")
  }
elif(e < 0):
  {
    print("the number is negative")
  }
else:
    print("the number is positive")
f=int(input("enter a year "))
if(f%4==0):
 {
     print("its a leap year")
 }
else:
     print("it's not a leap year")
g=int(input("enter the starting point"))
h=int(input("enter the ending point"))
for n in range(g,h+1):
   if n > 1:
       for i in range(2,n):
           if (n % i)==0:
               break
       else:
           print(n)
nterms = int(input("How many terms? "))
n1=1
n2=0
count=0
if nterms<=0:
   print("Please enter a positive integer")
elif nterms==1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
num=int(input("Enter a number: "))
sum=0
temp=num
while temp>0:
   digit=temp%10
   sum+=digit**3
   temp//=10
if num==sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
"""
num =int(input("enter the range"))
if num<0:
   print("Enter a positive number")
else:
   sum=0
   while(num > 0):
       sum+=num
       num-=1
   print("The sum is",sum)

     