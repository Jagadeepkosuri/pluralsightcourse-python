print("----for loops----")
stud_name=["Mark","John","James","Lee"]
for name in stud_name:
    print("Student name is {0}".format(name))

print("--specifying range in loops------")
print("----Range functions makes a list a numbers, indicating how many times the loop shoul iterate--------")
x=0
for index in range(10):           # Range indicates how many times the loop must be iterated => [1,2,3,.....9]
    x+=10
    print("The value of x is {0}".format(x))
print("-------------")
y=0
for index in range(5,10):       # Range starts from 5 and ends at 9 => [5,6,7,8,9]
    y+=10
    print("The value of y is {0}".format(y))
print("-------------")
z=0
for index in range(5,10,2): # Range can have three arguments. First argument is start point, the second one is end point and the third one is increment value (by how many times, it should increment))
    z+=10                                    # =>[5,7,9]
    print("The value of z is {0}".format(z))
print("-------using break and continue--------")

stud_name.append("Ricky")
stud_name.append("Chris")
stud_name.append("Root")
stud_name.append("Daniel")
stud_name.append("Joseph")
stud_name.append("Devilliers")
stud_name.append("Trot")
stud_name.append("Stuart")
print(stud_name)
for name in stud_name:
    if name=="Chris":
        print("Found {0}".format(name))
    print("Currently testing {0}".format(name))

print("--------break------------")

for name in stud_name:
    if name=="Chris":
        print("Found {0}".format(name))
        break        #this break will help us to stop iterating, since we found the desired element
    print("Currently testing {0}".format(name))
print("---------continue---------")

for name in stud_name:
    if name=="Chris":
        continue             # This continue will skip executing the block for this iteration and continue for the next values
        print("Found {0}".format(name))
    print("Currently testing {0}".format(name))

print("-----while loop-----")
i=0
while i<10:
    print("Value of i is {0}".format(i))
    i+=1
    


