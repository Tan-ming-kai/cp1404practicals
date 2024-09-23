total = 0
count = 0
age_of_member= int(input("Enter your age: "))


while age_of_member >=0:
    total = total + age_of_member
    count = count + 1
    age_of_member = int(input("Enter your age: "))

print(f"the total age of your family members is {total}")
average_age = total/count
print(f"your family has the average of {average_age} years old")

