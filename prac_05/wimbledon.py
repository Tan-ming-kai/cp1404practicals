"""
Wimbledon
Estimate: I forgot to give a estimate :(
Actual: 20 Mins
"""

champion_name_to_titles = {}
database_of_champions = []
winning_countries = set()

def main():

    extract_data_to_list()
    extract_name_and_trophy()

    # Displays output of wimbledon winners
    print("Wimbledon Champions")
    for name, trophy_count in champion_name_to_titles.items():
        print(f"{name}: {trophy_count}")
    print() # Adds a blank line
    extract_winning_countries()
    format_country_winners()


def extract_winning_countries():
    """extracts winning countries to a set """
    for country in database_of_champions:
        winning_countries.add(country[1])


def extract_data_to_list():
    """Reads file and appends all the data to a nested list"""
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # removes header from csv file
        for line in in_file:
            # append each line as a list into a bigger list
            database_of_champions.append(line.strip().split(","))


def extract_name_and_trophy():
    """Adds the name to a dictionary and counts the total trophies won by the same player"""
    for name in database_of_champions:
        # Adds the name and number of titles to a dictionary
        champion_name_to_titles[name[2]] = champion_name_to_titles.get(name[2], 0) + 1


def format_country_winners():
    """formats the output of the countries who have won wimbledon"""
    output = ", ".join(sorted(winning_countries))
    print(f"These {len(winning_countries)} countries have won Wimbledon: \n{output}")



main()