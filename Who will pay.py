# This program will determine who will pay for today's dinner :D
#split string mathod
import random

names_string = input("Give me everyone's name, seperated by a comma: ")
names = names_string.split(", ")

number_of_person = (len(names))
random_choice = random.randint(0, number_of_person - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to pay for the dinner today!! :D")