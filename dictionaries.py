#  Dictionaries are useful for storing some kind of structured data. They contain key value pairs. Dictionaries that contain dictionaries as keys re called Nested Dictionaries.
student={
    "name":"Mark",
    "id":525,
    "feedback":None

}
print(student)

print("----List containing dictionaries----")
all_students=[
    {"name":"James","id":526},
    {"name":"Johnathan","id":527},
    {"name":"John","id":528}
]
print(all_students)
print(student.keys())
print(student.values())
del all_students[0]
print(all_students)
