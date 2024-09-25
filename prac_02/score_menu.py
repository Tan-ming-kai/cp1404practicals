
menu = """G - Get a valid score
P - Print Result
S - Show stars
Q - Quit
>>>"""


def main():
    score = float(input("Enter score between 0 and 100: "))
    score = score_checker(score)
    print(menu)
    user_choice = input("Enter your choice: ").upper()

    while user_choice != "Q":
        if user_choice == "G":
            score = float(input("Enter score between 0 and 100: "))
            score = score_checker(score)
        elif user_choice == "P":
            print(f"Your Grade is {grade_calculator(score)}")
        elif user_choice == "S":
            print(int(score) * "*")
        else:
            print(f"{user_choice} is not a valid option")
        print(menu)
        user_choice = input("Enter your choice: ").upper()


def score_checker(score):
    while score < 0 or score > 100:
        score = float(input("Enter a valid score: "))
    return score


def grade_calculator(score):
    score = score_checker(score)
    if score >= 90:
        grade = "Excellent"
        return grade

    elif score >= 50:
        grade = "passable"
        return grade

    else:
        grade = "Bad"
        return grade


main()