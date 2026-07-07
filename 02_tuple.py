my_tuples = (5,1,3,5,6)
## Tuples uses parenthesis () to store values.
#* t1 = ()  list = []
print(my_tuples)

## Tuples are immutable, ordered
#% Access tuple elements with brackets []
print("2nd index value is: ",my_tuples[2])

fruits = ("Apple", "Banana", "Orange", "Mango", "Apple")
## How many times Apple repeats?
print("Apple repeat times: ", fruits.count("Apple"))

print("index of mango is: ",fruits.index("Mango"))

## Convert tuple to a list
fruits_list = list(fruits)
print(fruits_list)

## Convert list to a tuple
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

student = ("ilayaraja", 32, "Vellore")
name, age, city = student
print(f"{name} is {age} old living in {city}")