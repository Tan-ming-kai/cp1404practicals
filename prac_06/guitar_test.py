"""
guitar_test
Estimate: 15 minutes
Actual: 15 minutes
"""

from prac_06.guitar import Guitar


gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2020, 10000.00)


print(f"gibson get_age() - Expected 102. Got {gibson.get_age()}")
print(f"another_guitar get_age() - Expected 4. Got {another_guitar.get_age()}")

print(f"gibson is_vintage() - Expected True. Got {gibson.is_vintage()}")
print(f"another_guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

