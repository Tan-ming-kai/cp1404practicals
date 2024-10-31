HEXCODE_TO_COLOUR = {"ABSOLUTE ZERO": "#0048ba", "ACID GREEN": "#b0bf1a", "ALICEBLUE": "#f0f8ff",
                     "ALIZARIN CRIMSON": "e32636", "AMARANTH": "#e52b50", "AMBER": "#ffbf00", "AMETHYST": "#9966cc",
                     "ANTIQUEWHITE": "#faebd7", "APRICOT": "#fbceb1", "AQUA": "#00ffff"}

colour_choice = input("Enter colour: ").upper()

while colour_choice != "":
    if colour_choice in HEXCODE_TO_COLOUR:
        print(f"{colour_choice} --> {HEXCODE_TO_COLOUR[colour_choice]}")
    else:
        print("Invalid choice")
    colour_choice = input("Enter colour: ").upper()
