# use an if statement to show that divine weighs more than craig
# hint: print your results
divineWeight = 100
craigWeight = 75

if divineWeight > craigWeight:
    print("divine is heavier than craig")
else:
    print("craig is heavier than craig")

# use an elif statement to prove that shalom weighs more than craig but the same
# as mitch and an else statement to handle any weird cases
mitchWeight = 100
shalomWeight = 100
craigWeight = 75
elephantWeight = 1000

if shalomWeight is craigWeight:
    print("shalom weighs more than craig")
elif shalomWeight is mitchWeight:
    print("shalom is the same weight as mitch")
else:
    print("elephants weight is not necassary")

# the woman wants a younger man how can we give her one
man1 = {"age": 23}
woman1 = {"age": 40}
if man1["age"] >= woman1["age"]:
    print("too old to marry the woman")
else:
    print("young enough to marry the woman")
