#python basics:tokens,statements,identifiers,variables,keywords
#1.tokens
x=30
name="Akhila"
print("Tokens:",x,name,x+5)
print("smallest individual unit in a program")
print()
#2.statements
x=10
print("statements:",x)

if x>5:
    print("x is greater than 5")

#3.comments
print("comments are used to explain code")
#single line comments
print("# is used for single line comment")

#multiline comments
"""these are used fofr multiline comments"""

#4.variables
number=10
language="Python"
price=3.14
print("variables :",number,language,price)

#5.multiple assignment
a,b,c=10,20,30
print("multiple assignment: ",a,b,c)

x=y=z=100
print("same value assignment : ",x,y,z)

#6.Reassignment
x=5
x=10
print("Reassignment : ",x)

#7.Swapping
a=10
b=20
a,b=b,a
print("after swapping a:",a)
print("after swapping b:",b)

#8.Deleting variables
value=50
del value
print("variable deleted sucessfully")

#9.keywords
import keyword

print("python keywords:")
print(keyword.kwlist)
