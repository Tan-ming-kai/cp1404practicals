from random import *

def main():
    score = float(input("Enter score: "))
    result_comment = get_user_score(score)
    print(result_comment)


def get_user_score(score):
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

# I'm not too sure if the question is asking me to also pass the random score into grade checker also?

random_score_generator =  randint(1,100)
print(random_score_generator)
main()
