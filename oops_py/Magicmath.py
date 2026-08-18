class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


s1 = Student("Anubhav", 20)

print(s1)


# Magic Method	Purpose
# __init__()	Initializes an object
# __str__()	Controls what print(object) displays
# __repr__()	Developer-friendly representation
# __len__()	Defines behavior of len(object)
# __add__()	Defines object1 + object2
# __sub__()	Defines object1 - object2
# __eq__()	Defines object1 == object2
# __lt__()	Defines object1 < object2
# __gt__()	Defines object1 > object2

