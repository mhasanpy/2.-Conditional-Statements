# practice_02_conditionals.py
"""
Conditional Statements Practice
"""

# Exercise 1: Even or Odd
print("=== Exercise 1: Even or Odd ===")
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Test the function
for num in [7, 12, 23, 44, 51]:
    print(check_even_odd(num))

# Exercise 2: Grade Calculator
print("\n=== Exercise 2: Grade Calculator ===")
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test scores
scores = [95, 85, 75, 65, 55]
for score in scores:
    print(f"Score: {score} → Grade: {calculate_grade(score)}")

# Exercise 3: Leap Year Checker
print("\n=== Exercise 3: Leap Year ===")
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

years = [2000, 2004, 1900, 2020, 2023]
for year in years:
    print(f"{year} is {'a leap year' if is_leap_year(year) else 'not a leap year'}")

# Exercise 4: Maximum of Three Numbers
print("\n=== Exercise 4: Maximum of Three ===")
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(f"Max of (15, 27, 9) is: {find_max(15, 27, 9)}")
print(f"Max of (100, 50, 75) is: {find_max(100, 50, 75)}")