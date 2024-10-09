from random import *
def main():
    quick_pick_output = []
    number_of_quick_picks = input("How many quick picks ")
    generate_quick_picks(number_of_quick_picks,quick_pick_output)
    print(quick_pick_output)


def generate_quick_picks(number_of_quick_picks,quick_pick_output):
    """generates numbers in quick picks and stores them in a list and appends that list to the total list of quick picks"""
    for i in range(0, int(number_of_quick_picks)):
        quick_picks = []
        for j in range(0, 6):
            quick_picks.append(randint(1, 45))

        quick_picks = list(dict.fromkeys(quick_picks))

        while len(quick_picks) != 6:
            # checks for duplicates and delete them if present
            quick_picks.append(randint(1, 45))
            quick_picks = list(dict.fromkeys(quick_picks))

        quick_pick_output.append(quick_picks)


main()