students=[
    ("Ravi","Gupta"),
    ("Pooja","Yadav"),
    ("Sunil","Shetty"),
    ("Anu","Sharma"),
    ("Neha","Joshi"),
    ("Vijay","Mishra"),
    ("Pooja","Patil"),
    ("Ankita","Patil"),
    ("Manoj","Das"),
    ("Arun","Yadav"),
    ("Arjun","Nair"),
    ("Rahul","Shinde"),
    ("Sita","Rao"),
    ("Mina","Patel"),
    ("Anuj","shaha"),
    ("Neharika","chahvan"),
    ("Rekha","Patil"),
    ("Neha","Joshi"),
    ("Omkar","Pawar"),
    ("Shweta","Mohite")
]

unique_students={}

for fname,lname in students:
    if fname not in unique_students:
        unique_students[fname]=lname

print("Students after removing duplicates(same name, different surname): ")
for fname,lname in unique_students.items():
    print(fname,lname)
print("Final count of students: ",len(unique_students))
    
