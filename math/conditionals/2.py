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

studentScore = 53
if studentScore > 89:
    print("A+")
elif studentScore > 75 and studentScore < 79:
    print("B+")
elif studentScore > 50 and studentScore < 55:
    print("C+")
else:
    print("D")

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


salary = 69000
deduction = 0  # if only

if salary > 220000:
    deduction = 13.16
elif salary > 150001 and salary < 220000:
    deduction = 12.16
elif salary > 89483 and salary < 150000:
    deduction = 11.16
elif salary > 44741 and salary < 89482:
    deduction = 9.15
else:
    deduction = 5.05

printNewSalary(salary, deduction)
