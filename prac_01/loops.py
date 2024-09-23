for i in range(1, 21, 2):
    print(i, end=' ')
print()

#question a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#question b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#question c
user_number_of_stars = int(input("Enter number of stars: "))

for i in range(1, user_number_of_stars + 1):
    print("",end='*')

# question d
print("\n")
end_string = ''
number_of_stars = 0
adding_stars=[]
for stars in range(1, user_number_of_stars + 1):
    adding_stars.append("*")
    end_string = "".join(adding_stars)
    print(end_string)


for J in range(1,number_of_stars+1,1):
    print("*" * J)
print()








