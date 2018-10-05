stud_name=["Mark","John","Lee"]
print(stud_name)
print(stud_name[0])
print(stud_name[2])
print(stud_name[-1])
stud_name[0]="James"  # Negative indexing will start from -1.The last element in the list will have index as -1."""
print(stud_name)
stud_name.append("Homer") # Add to the end
print(stud_name)
p="Mark" in stud_name   # To check if element is present in list or not
if p:
    print("Mark is present in the student list")
else:
    print("Mark is not present in the list")
print("-----len function in python------")
q=len(stud_name)      # Length of list
print("Length of list is {0} ".format(q))
r=len("Jagadeep")      # Length of the string
print("Length of the string is {0} ".format(r))
del stud_name[2]
print(stud_name)
print(stud_name[1:])
print(stud_name[1:2])
print(stud_name[1:-1])
print(stud_name[0:-1])
