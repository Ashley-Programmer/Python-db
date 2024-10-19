# define class
class Person:

    # dunder method -> (__init__)
    # self variable reference to the object
    def __init__(self, firstname, lastname):
        # below are attributes
        self.fn = firstname
        self.ln = lastname
        self.fullname = f"{firstname} {lastname}"


# create an object
# treat it like a method
# p is an object
p = Person("Ashley Koketso", "Motsie")

# access each attribute by its name
print(f"First Names: {p.fn}")
print(f"Last Name: {p.ln}")
print(f"Full Names: {p.fullname}")
print("******_________********")
print(f"Hello {p.fullname} welcome to OOP programming")
print("******_________********")
