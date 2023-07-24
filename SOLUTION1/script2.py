#Write a python script to enter any number and print the sum of its dig.
r=int(input("Enter any number:"))
s=0
while(r>0):
    c=r%10
    s=s+c
    r=r/10
print("sum of digit of no {}is{}".format(a,sum))   
