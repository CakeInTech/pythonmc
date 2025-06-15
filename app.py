# declaring variables

name = "Mohamed"
age = 21
height =  5.9

name= "abdul"
age = 25
height = "five ft, 2 inches"

# printing variables
print(name, age, height)

# type errors
print(name + str(age))
print (10 + int("20"))

# string methods
greeting = " Hello, World! "


print(len(greeting))
print(greeting.strip())
print(greeting.strip().lower())
print(greeting.strip().upper())
print(greeting.replace("Hello", "Yo").strip())
print(greeting)

# Lists
fruits = ["apple", "banana", "cherry"]

print(fruits[0])
print(fruits[1])
print("The length of the list is ", len(fruits))
# changing the value of a list
fruits[1] = "orange"
print(fruits)
# list method
fruits.append("kiwi")
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.sort()
print(fruits)

# tuples
top_scores = (100, 90, 80)
print(top_scores[0])
print(top_scores[1])
print("The length of the tuple is ", len(top_scores))

# tuples are immutable
# top_scores[0] = (20)

# tuple methods
print(top_scores.count(90))
print(top_scores.index(80))

