# ASSIGNMENT NAME: Decision-making program
"""
Build: a decision-making program independently.
• Ask for at least 3 pieces of information.
• Convert numeric input correctly.
• Use comparisons.
• Use if/elif/else.
• Use at least one logical operator.
• Use an f-string for readable output.
• Test at least 5 cases.
• Include at least one boundary case.
• Make at least 3 meaningful Git commits.
• Be able to explain every condition.
Possible projects: grade classifier, ticket eligibility, scholarship checker, discount calculator, age classifier,
transport fare decision system
"""
print("Grade Classifier")

# User Information
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
name = first_name + " " + last_name
print(name)
score = int(input("Score in Math: "))

# CONDITION CHECK
if score >= 0 and score <= 39:
    grade = "F"
    remark = "Fail"
elif score > 39 and score <= 49:
    grade = "D"
    remark = "Pass"
elif score > 49 and score <= 59:
    grade = "C"
    remark = "Credit"
elif score > 59 and score <= 69:
    grade = "B"
    remark = "Good"
elif score > 69 and score <= 100:
    grade = "A"
    remark = "Excellent"
else:
    grade = " "
    remark = "Not a score"