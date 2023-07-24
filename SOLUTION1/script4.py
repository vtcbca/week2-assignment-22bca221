# Write a script to enter any number and check its armstrong number or not.
a=int(input("enter any number"))
s=0
temp=a
while(a>0):
     b=a%10
     c=b*b*b
     a=a/10
     s=s=c
if(s==temp):
      print("{} is armstrong".format(temp))
else:
      print("number is not armstrong:")
      
