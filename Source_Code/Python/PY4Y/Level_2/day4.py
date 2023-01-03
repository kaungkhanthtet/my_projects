pet_name = {"Dog" : "wote_wote", "Cat" : "mhee_mhee", "Chicken" : "aw_eee_aut", "Age" : 9}
# print(pet_name)
# print(pet_name["Dog"])
# print(pet_name.get("Dog"))
# print(pet_name.keys())
# print(pet_name.values())

print("**********")

# if "Dog" in pet_name:
#     print("Yes")
# else:
#     print("NO")

# if "wote_wote" in pet_name.values():
#     print("Yes")
# else:
#     print("NO")

# if "wote_wote" in pet_name:
#     print("Yes")
# else:
#     print("NO")

print("**********")
#Adding new item

# pet_name["Crow"] = "ah_ah_ah"
# print(pet_name)

print("**********")
#Changing/Replacing an item

# pet_name["Age"] = 10
# print(pet_name)

# pet_name.update({"Age": "9", "Cat": "Mee-mee"})
# print(pet_name)

print("**********")
#Removing Specific item

# pet_name.pop("Dog")
# print(pet_name)

#Removing the last item

# pet_name.popitem()
# print(pet_name)

print("**********")
#Using del Keyword

# del pet_name["Dog"]
# print(pet_name)

print("**********")
#Delecting Dictionary

# del pet_name
# print(pet_name)

print("**********")
#Clearing the entires of a dictionary

# pet_name.clear()
# print(pet_name)

print("**********")
#Extracting the keys and values into their own lists

# keys_list = list (pet_name.keys())
# print(keys_list)
# values_list = list (pet_name.values())
# print(values_list)

print("**********")
#Looping a Dictionary

# for x, y in pet_name.items ():
#     print(x, y)

# for x in pet_name.keys():
#     print(x)

# for y in pet_name.values():
#     print(x)

print("**********")
#Dictionary Exercise

# TV = {"brand":"sony", "price":500000, "year":2015}
# print(TV.get("price"))

print("********** \n********** \n**********")
#Set

fruit = {"apple", "banana", "orange"}
print(fruit)

print("**********")
#Accessing the Set's item

# for x in fruit:
#     print(x)

print("**********")
#Checking the existence of data in Set
#Way 1

# if "apple" in fruit:
#     print("Yes")
# else:
#     print("No")

#Way2

# print("apple" in fruit)

print("**********")
#Adding new item into Set

# fruit.add("Cherry")
# print(fruit)

#Adding new set into old Set

# price ={10, 2, 4, 5}
# fruit.update(price)
# print(fruit)

print("**********")
#Removing an item

# fruit.remove("apple")
# print(fruit)
# fruit.discard("banana") #discard() will raise an error if item is not present.
# print(fruit)

print("**********")
#Delecting all items in a Set

# fruit.clear()
# print(fruit)

# Delecting a Set

# del fruit
# print(fruit)

print("**********")






