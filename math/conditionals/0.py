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
