fruits = ["apple", "banana", "mango", "orange", "strawberry"]

i = 0
for fruit in fruits:
    print(f"{i}. {fruit.title()}")
    i = i+1

fruits.append("pineapple")

other_fruits=["grapes","musk melon", "water melon"]
fruits.extend(other_fruits)
print(fruits)
print("Total Fruits: ",len(fruits))

fruits.insert(2, "lemon")
print(fruits)

fruits.remove("orange")
print(fruits)

# fruits.remove("test") ## throws value error
try:
    fruits.remove("test")
except Exception as e:
    print("Error: ", e)

print("")
#% removes and return the last element
item = fruits.pop()
print(item)

#% removes and return the element at index
another_item = fruits.pop(0)
print(another_item)

print(fruits)
print(fruits.index("strawberry"))
print(fruits.count("lemon"))
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

list_new = fruits.copy()
print(list_new)
list_new.insert(0, "Apple")
print(list_new)
print(fruits)