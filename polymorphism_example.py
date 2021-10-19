# len does a great job demoing polymorphism
# you can chuck a single string at it, a dictionary or even a list
# len can handle "many forms" and still give answers

name = "Jim"
print(len(name))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict["brand"]))

some_list = ["some","name"]
print(len(some_list))

# Answers
# 3
# 4
# 2
