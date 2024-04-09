class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says: Woof woof!")

class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"Hello, my name is {self.name}.")

# Creating instances of the Person class
person1 = Person("Alice")
person2 = Person("Arthur")

# Creating instances of the Dog class
dog1 = Dog("Wrigley")
dog2 = Dog("Truman")

# Calling the introduce method of the Person instances
person1.introduce()  # Output: Hello, my name is Alice.
person2.introduce()  # Output: Hello, my name is Arthur.

# Calling the bark method of the Dog instances
dog1.bark()  # Output: Wrigley says: Woof woof!
dog2.bark()  # Output: Truman says: Woof woof!
