"""
emails
Estimate: 20 mins
Actual: 25 mins
"""


email_to_name = {"bob@gmail.com":"Bob The Builder","manny@gmail.com":"Manny ","hello@gmail.com":"Mary"}
output_email_to_name = {}
user_email = input("Enter your email: ")

def main():
    print()

for email in email_to_name:
    if email == user_email:
        verification = input(f"Is your name {email_to_name[email]}? (y/n) ")
        if verification == "y" or verification == "":
            name = email_to_name[email]
            output_email_to_name[email] = name
            user_email = input("Enter your email: ")
        else:
            name = input("Enter your name: ")
            output_email_to_name[email] = name

for email,name in output_email_to_name.items():
    print(f"{name} ({email})")


main()



