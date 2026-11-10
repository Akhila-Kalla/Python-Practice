"""Develop a voting eligibility application. 
Accept the following details from the user:
 • Person's name • Age • Country 
Display the person's name and eligibility status"""
name=input("Enter Name : ")
age=int(input("Enter Age : "))
Country=input("Enter Country : ")
if age>18:
    print(f"{name} in {Country} is Eligible for vote")
else:
    print(f"{name} in {Country} is Not eligible for vote")