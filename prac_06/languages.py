"""
languages
Estimate: 15 minutes
Actual: 15 minutes
"""
from prac_06.programming_language import ProgrammingLanguages


def main():
    python = ProgrammingLanguages("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguages("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguages("Visual Basic", "Static", False, 1991)
    print(python)
    print(ruby)
    print(visual_basic)
    print()  # empty line so that the output looks nicer

    languages = [ProgrammingLanguages("Python", "Dynamic", True, 1991),
                 ProgrammingLanguages("Ruby", "Dynamic", True, 1995),
                 ProgrammingLanguages("Visual Basic", "Static", False, 1991)]

    dynamic_languages = gets_dynamic_languages(languages)

    print("The dynamically typed languages are:")

    for dynamic_language in dynamic_languages:
        print(dynamic_language)


def gets_dynamic_languages(languages):
    """gets all dynamic languages and stores it into a list called dynamic_languages"""
    dynamic_languages = []
    for language in languages:
        if language.is_dynamic():
            dynamic_languages.append(language.language_name)
    return dynamic_languages


main()
