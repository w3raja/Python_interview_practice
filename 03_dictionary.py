student = {
    "name" : "Ilayaraja",
    "age" : 32,
    "city" : "Vellore"
}

print(student)
print(student["name"])

# throws error if key is not found
# print(student["state"])

print(student.get("name"))
print(student.get("state")) ## No error. simply 'None'

print()
print(student.keys())
print(student.values())

## Returns list of keys and values pairs
print("keys and values: ", student.items())

print()
student.update({"role":"Data Engineer"})

print()
for keys, values in student.items():
    print(f"{keys} is {values}")

student.pop('city')
print("\n",student)

## Removes and return LAST inserted key value pair
print(student.popitem())

print(student)
student.clear()
print(student)

student["name"] = "Venkat"
student["age"] = 38
print(student)

if "name" in student:
    print("name is exists")
    del student["name"]
    print(student)
