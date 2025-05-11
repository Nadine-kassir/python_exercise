x=""
num=""
check =""
x=int(input("enter a number:"))
if x % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

if x % 4 == 0:
    print("The number is multiple by 4.")
num=int(input("entre a number to check :"))
check=int (input("entre a number to devided by: "))
if num % check == 0 :
    print (f"the number  {num } is devided by {check}")
