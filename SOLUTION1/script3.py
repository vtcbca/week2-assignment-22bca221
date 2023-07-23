# Write a python script to enter any number,if it is interger number,then check its palindrome or not.Print appropriate message if it is not palindrome.
s=int(input("Enter any number:"))
a=s
r=0
while(r>0):
    digit=n%10
    r=r*10+digit
    s=s//10
print(s)
if r==a:
    print("number is palindrome")
else:
    print("number is not palindrome")
    
