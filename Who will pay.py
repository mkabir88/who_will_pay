# This program will determine who will pay for today's dinner :D
#split string mathod
import random

names_string = input("Give me everyone's name, seperated by a comma: ")
names = names_string.split(", ")

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to pay for the dinner!")

#this is v2