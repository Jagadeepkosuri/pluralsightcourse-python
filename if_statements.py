print("--------if conditions-------")
number=4
if number==5:
    print("Number is 5")
else:
    print("Number is not 5")

print("---------")
num=5
if num:
    print("Number is defined and truthy")
text="Python"
if text:
    print("Text is defined and truthy")
print("---------")
val=0
if val:
    print("Value is defined and truth")
else:
    print("Value is not defined and not truthy")
str=" "
if str:
    print("String is defined and truthy")
else:
    print("String is not defined and not truthy")
print("---------")
p=True
if p:
    print("No need to compare p by using == sign with True")
aliens_found=None
if aliens_found:
    print("This will not print")
else:
    print("This else statement will be executed because the if condition will not be satisfied")
print("----------")
python_course=False
if not python_course:
    print("This will execute because python_course is set to false and it is if not condition")
print("--------Multiple if conditions---------")
q=3
r=True
s=False
if q==2 and r:
    print("This will execute since two variables are true")
else:
    print("This will execute if both the conditions are not satisfied")

if q or s:
    print("This will execute because atleast one variable is true")
print("------Ternary if statement--------")
print("bigger" if number>q else "smaller")