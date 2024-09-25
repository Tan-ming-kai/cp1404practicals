# """
# CP1404/CP5632 - Practical
# Broken program to determine score status
# """
#
#
# score = float(input("Enter score: "))
#
# if score < 0:
#     print("Invalid score")
#
# else:
#     if score > 100:
#         print("Invalid score")
#     elif score >= 90:
#         print("Excellent")
#     elif score >= 50:
#         print("passable")
# if score < 50:
#     print("Bad")
from unicodedata import category



def main():
    result_comment = get_user_score()
    print(result_comment)


def get_user_score():
    score = float(input("Enter score: "))
    if score < 0 or score >100:
        grade = "Enter a valid score"
        return grade

    elif score >= 90:
        grade = "Excellent"
        return grade

    elif score >=50:
        grade = "passable"
        return grade

    else:
        grade = "Bad"
        return grade


main()