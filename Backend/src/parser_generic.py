import abc

""" abc - abstract class Module
an abstract class is a blueprint for other classes, and it can contain abstract methods,
 which are methods declared but not implemented. You use abstract classes and methods 
 to define interfaces or base classes that other classes must implement"""


class MedicalDocParser(metaclass=abc.ABCMeta):
    def __init__(self, text):
        self.text = text

    @abc.abstractmethod
    def parse(self):
        pass

# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):

#     def sound(self):
#         return "Bark"

# class Cat(Animal):

#     def sound(self):
#         return "Meow"

# # Create instances of Dog and Cat
# dog = Dog()
# cat = Cat()

# print(dog.sound())  # Output: Bark
# print(cat.sound())  # Output: Meow

# Abstract classes can't be instantiated directly, and subclasses must provide implementations for the abstract methods.
