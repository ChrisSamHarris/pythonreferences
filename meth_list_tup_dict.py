# METHODS
method = "hello there".upper()
print(method)

greeting = "hello there"
print(greeting.title()) 
# ^ Executes the new code but doesnt update the original 
greeting = greeting.title()
# ^ perm updates the greeting variable


shopping_list = ['vinegar', 'apples', 'banana']
shopping_list.append('coffee')
print(shopping_list)

# dir = Provides a list of methods that can be used on an class: string, list, tuple, dict etc.. 
# print(dir("test_string"))
print(len(dir("test_string")))

# List & Tuples
list_var = ['vinegar', 'apples', 'banana']
tuple_var = ('alvarez', 'football', 'haaland', 'man city') # Tuples are immutable - They can not be modified 

print(tuple_var[2])
print(tuple_var[2].title())
print(tuple_var[1:3]) 
# Slicing = Up to , but nopt including index 3 in this example 

string_den = 'Denmark'
print(string_den[-2])

# Dictionaries

john = {"first_name": "John", "last_name":"Smith", "age":40}
persons = {"first_name": ["john", "laura", "debbie"],
           "last_name": ["smith", "eager", "michaels"],
           "age": [40, 25, 68]}

print(john["first_name"])
print(persons["last_name"][0].capitalize())





