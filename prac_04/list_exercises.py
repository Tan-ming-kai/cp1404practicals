
def main():
    numbers = []
    numbers = get_user_numbers(numbers)
    print(numbers)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers)/len(numbers)}")


def get_user_numbers(numbers):
    """gets user numbers and appends to a list"""
    for i in range(0,5):
        user_number = int(input("Enter a number: "))
        numbers.append(user_number)
    return numbers




main()