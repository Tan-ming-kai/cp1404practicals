

champion_name_to_titles = {}
database_of_champions = []
winning_countries = set()



with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    in_file.readline() # removes header from csv file
    for line in in_file:
        #append each line as a list into a bigger list
        database_of_champions.append(line.strip().split(","))

for name in database_of_champions:
    # Adds the name and number of titles to a dictionary
    champion_name_to_titles[name[2]] = champion_name_to_titles.get(name[2],0) +1

for country in database_of_champions:
    winning_countries.add(country[1])

print("Wimbledon Champions")
for name,trophy_count in champion_name_to_titles.items():
    print(f"{name}: {trophy_count}")

output = ", ".join(sorted(winning_countries))
print(f"These {len(winning_countries)} countries have won Wimbledon: \n{output}")
