student = {
    "name":"sohel",
    "age":15
}
keys = student.keys()
values = student.values()
items = []
for item in range(len(keys)):
    items.append((keys[item], values[item])) 
print(items)
print(student.items())