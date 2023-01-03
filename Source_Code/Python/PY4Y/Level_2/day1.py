# first_name = "Kaung"
# middle_name = "Khant"
# last_name = "Htet"
# full_name = first_name+" "+middle_name+" "+last_name

# print(full_name)

# print("**********")

# print(3 * "Hello ")

# print("**********")

# txt = "Hello!"

# if "e" in txt:
#     print("e is in txt")
# else:
#     print("Blah...")

# print("**********")

# txt = "Hello!"

# if "!" not in txt:
#     print("Blah...")
# else:
#     print("! is in txt")

# print("**********")

# list1 = [1, 2, 3, 5, 0]
# list2 = [1, 2, 3, 5, 0]

# if list2 is list1:
#     print("They're in the same location")
# else:
#     print("Sorry, they aren't in the same location ")

# print(id(list1))
# print(id(list2))

# print("**********")

# txt = "HELLO, GUYS"
# print(len(txt))

# print("**********")

# txt = "hello My Friends"
# print(txt.lower())
# print(txt.islower())

# txt = "Hello my friends"
# print(txt.upper())
# print(txt.isupper())

# print("**********")

# txt = "hello My Friends"
# print(txt.capitalize())
# print(txt.title())
# print(txt.swapcase())

# print("**********")

# txt = "Hello, welcome to my python class"
# print(txt.find("welcome"))
# print(txt.find("e"))
# print(txt.find("e", 5, 10))

# print(txt.index("welcome"))
# print(txt.index("e"))
# print(txt.index("e", 5, 10))


# print("**********")

# txt = "One Two Three One Two Three One Two Three"
# print(txt.replace("One", "Three"))

# print("**********")

# #Type 1
# txt = "Hello, my name is, TT"
# print(txt.split(","))
# #Type 2
# txt = "Hello, my name is TT"
# print(txt.split())

# print("**********")

# #Positive
# txt = "Hello World"
# slic_txt = txt[5:9]
# print(slic_txt)
# #Negative
# txt = "Hello World"
# slic_txt = txt[-5:-1]
# print(slic_txt)

# print("**********")

# a = " Hello, World! "
# print(a.strip()) 

# print("**********")

# #Way 1
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
# #Way 2
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# print("**********")
# # Python - Slicing Strings (w3schools.com)
# # Python String split() Method (w3schools.com)
import random

normaltc_m = ['End of Cycle', 'Beginnings', 'Change', 'Metamorphosis','Reflection', 
    'reckoning', 'Awakening', 'Cause and Effect', 'Clarity', 'Truth', 'inner strength', 
    'bravery', 'compassion', 'focus', 'middle path', 'patience', 'finding meaning', 
    'direction', 'control', 'willpower', 'addiction', 'materialism', 'playfulness', 'authority', 
    'structure', 'control', 'fatherhood', 'motherhood', 'fertility', 'nature', 'innocence', 'new beginnings', 
    'free spirit', 'sacrifice', 'release', 'martyrdom', 'contemplation', 'search for truth', 'inner guidance', 
    'tradition', 'conformity', 'morality', 'ethics', 'intuitive', 'unconscious', 'inner voice', 'partnerships', 
    'duality', 'union', 'willpower', 'desire', 'creation', 'manifestation', 'unconscious', 'illusions', 
    'intuition', 'hope', 'faith', 'rejuvenation',  'joy', 'success', 'celebration', 'positivity', 
    'sudden upheaval', 'broken pride', 'disaster', 'fulfillment', 'harmony', 'completion', 
    'change', 'cycles', 'inevitable fate']
One = '_1'
for i in normaltc_m:
    print(i+One)
    
print('My name is'+'Kevin')

# new_normaltc_m = []  
# for i in normaltc_m:
#     new_normaltc_m.append(i.title())

# m = new_normaltc_m[10:13]
# random_taker = random.randrange(0,3)
# result = m[random_taker]
# print(result)

 
# print(new_normaltc_m)
# print(new_normaltc_m[0:3])
# print(new_normaltc_m[3:6])

# txt = "hello my friends"
#print(txt.capitalize())
# print(txt.title())
#print(txt.swapcase())