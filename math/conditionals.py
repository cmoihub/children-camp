"""
    Conditionals help the computer to take multiple decisions based on what
    we tell it
    It's like how your parents give you food if you're hungry
    If you're not something else should happen (of course some people eat regardless
    of whether they're hungry or not, which is why they blow up like balloons
    but that's another day's story, read 3 John 1:2 && 1 Cor 6:12 for more)

    The goal of this exercise is to have you play around with conditionals via
    if, elif & else combos
    And also nesting conditionals 🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪🤪
"""

condition = True
if condition:
    print("condition met")
# convert the following to an else statement
if not condition:
    print("condition not met")

# elif = if the previous conditions were not true, then try this condition
meals = 3
condition1 = meals == 3
condition2 = meals > 5
if condition1:
    print("I've got enough meals")
elif conditon2:
    print("I've got too much to eat")
else:
    print("I'm small and I love it")

# use an if statement to prove that divine weighs more than mitch
divineWeight = 100
craigWeight = 75

# use an elif statement to prove that shalom weighs more than craig but the same
# as mitch and an else statement to handle any weird cases
mitchWeight = 100
shalomWeight = 100
craigWeight = 75
elephantWeight = 1000

# the woman wants a younger man how can we give her one
man1 = {"age": 40}
woman1 = {"age": 40}
if man1["age"] >= woman1["age"]:
    print("too old to marry the woman")
else:
    print("young enough to marry the woman")

# Exercises
# a student got a score of 53/100 on a test, what is his grade?
# use ifs, else ifs & elses to show
# we'll start it off for you

"""
Letter	Percent
A+	    90%–100%
A	    85%–89%
A-	    80%–84%
B+	    75%–79%
B	    70%–74%
B-	    65%–69%
C+	    60%–64%
C	    56%–60%
C-	    50%–55%
D	    0%–49%
"""

studentScore = 20
if studentScore > 89:
    print("A+")
else:
    print("A")

# use ifs and elses to show if a number is negative or not

# identify my tax bracket
"""
5.05% on the first $44,740 of taxable income
9.15% on the next $44,741-$89,482
11.16% on the next $89,483-$150,000
12.16% on the next $150,001-$220,000
13.16 % on the amount over $220,000
"""

# ignore the function
def printNewSalary(salary, deduction):
    print(salary - salary * deduction / 100)


salary = 2652 * 13 * 2
deduction = 0  # if only

if salary > 220000:
    deduction = 13.16
else:
    deduction = 5.05

printNewSalary(salary, deduction)

# More CONDITIONALS!!!
# And & Or
# We use and to combine conditions
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# We use or to say if any condition is true you pass
soalaListened = False
soalaWasNice = True

if soalaListened or soalaWasNice:
    print("Soala is awesome")

# You can have an if in an if in an if in an if in another if in another...
jordanAge = 41

if jordanAge > 10:
    print("Jordan's older than 10 years old")
    if jordanAge > 20:
        print("Jordan's pretty old")
    else:
        print("Jordan's younger than 20 at least")

# There's also the pass statement
bored = True
if bored:
    pass

# Homework
print("what was your score in math")
age = input("--> ")
print(age)
"""
use nested if statements to show how good your grade was
whilst using if statements to show what the letter is

Letter	Percent
A+	    90%–100%
A	    85%–89%
A-	    80%–84%
B+	    75%–79%
B	    70%–74%
B-	    65%–69%
C+	    60%–64%
C	    56%–60%
C-	    50%–55%
D	    0%–49%

WOW! = A+, A, A-
YOU DID YOUR BEST = B+, B, B-
YOU PASSED = C+, C, C-
BETTER LUCK NEXT TIME = D

muahahahhahahahahhahahahahhahaha
"""
