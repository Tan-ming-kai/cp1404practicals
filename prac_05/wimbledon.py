"""
Wimbledon
Estimate: I forgot to give a estimate :(
Actual: 20 Mins
"""



def main():

    database_of_champions = extract_data_to_list()
    champion_name_to_titles = extract_name_and_trophy(database_of_champions)

    # Displays output of wimbledon winners
    print("Wimbledon Champions")
    for name, trophy_count in champion_name_to_titles.items():
        print(f"{name}: {trophy_count}")
    print() # Adds a blank line
    winning_countries = extract_winning_countries(database_of_champions)
    format_country_winners(winning_countries)


def extract_winning_countries(database_of_champions):
    """extracts winning countries to a set """
    winning_countries = set()
    for country in database_of_champions:
        winning_countries.add(country[1])
    return winning_countries


def extract_data_to_list():
    """Reads file and appends all the data to a nested list"""
    database_of_champions =[]
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # removes header from csv file
        for line in in_file:
            # append each line as a list into a bigger list
            database_of_champions.append(line.strip().split(","))

    return database_of_champions


def extract_name_and_trophy(database_of_champions):
    """Adds the name to a dictionary and counts the total trophies won by the same player"""
    champion_name_to_titles = {}
    for name in database_of_champions:
        # Adds the name and number of titles to a dictionary
        champion_name_to_titles[name[2]] = champion_name_to_titles.get(name[2], 0) + 1

    return champion_name_to_titles


def format_country_winners(winning_countries):
    """formats the output of the countries who have won wimbledon"""
    output = ", ".join(sorted(winning_countries))
    print(f"These {len(winning_countries)} countries have won Wimbledon: \n{output}")



main()