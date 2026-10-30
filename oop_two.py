# OOP solid principle and design patterns 
# oop is a programming approach that organizes code around objects.
# Class = a blueprint for creating objects.
# class BankAccount:
    # pass
# account1 = BankAccount()
# print(account1)
# class = "Blueprint of a house"
# Object = actual house built from that blueprint.
# The init method() used to initialize an object's attributes.
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw (self,amount):
        self.balance -= amount
account1 = BankAccount("Lydia", 500)
print(account1.owner)
# Self = refers to the cureent object.
# Methods in Python
# Amethod is a function defined inside a class.
# The four pillars of oop
# Encapusulation

class Person:
    def __init__(self,name,favorite_color):
        self.name = name
        self.__favorite_color = favorite_color
