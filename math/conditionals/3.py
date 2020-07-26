# More CONDITIONALS!!!
# And & Or
# We use 'and' to combine conditions
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# We use 'or' to say if any condition is true you pass
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
age = int(age)
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
