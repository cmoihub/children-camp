# Craig's
num = int(input(" how many elements do you want to the dictionary?"))
num = num * 2
a = {}
while num > 0:
    key = input("key:")
    value = input("value:")
    a[key] = value
    num -= 2

print(a)


num = int(input(" how many elements do you want in the dictionary"))
a = {"like": [], "dislike": []}
while num > 0:
    value = input()
    if "a" in value:
        a["like"].append(value)
    else:
        a["dislike"].append(value)
    num -= 1

print(a)

# Divine's
my_dict_1 = {}
like_list = []
dislike_list = []
my_dict_2 = {"I like these": like_list, "I don't like these": dislike_list}

num = int(input("How many elements do you want in first dictionary? "))

for i in range(num):
    print(i, end=" ")
    temp_key = input("enter an item: ")
    temp_val = input("do you like this item? y/n  ")
    if temp_val == "y":
        my_dict_1[temp_key] = "like"
    else:
        my_dict_1[temp_key] = "dislike"

print(my_dict_1)


num = int(input("How many elements do you want in second dictionary? "))

for i in range(num):
    print(i, end=" ")
    temp_val = input("enter an item: ")
    answer = input("do you like this item? y/n  ")
    if answer == "y":
        like_list.append(temp_val)
    else:
        dislike_list.append(temp_val)

print(my_dict_2)
