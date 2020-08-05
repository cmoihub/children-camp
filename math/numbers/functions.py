def linear_search(list, item):
    found = False
    for i in range(len(list)):
        if item == list[i]:
            found = True
            print("found")
        else:
            print(item, "still searching")
    if not found:
        print(item, "was never found")


def get_my_faves(number_of_faves=3):
    a = []
    for i in range(number_of_faves):
        a.append(input())
    return a


def length(list):
    count = 0
    for i in list:
        count += 1
    return count


def my_sum(list):
    count = 0
    for i in list:
        count += i
    return count


def greater(a, b):
    return a > b


def lesser(a, b):
    return a < b

