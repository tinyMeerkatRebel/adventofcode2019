import math

# Take the list of numbers and return an array of them
def parse(listNumbers):
    ans = []
    for listNumber in listNumbers:
        if listNumber:
            ans.append(int(listNumber))
    return ans

# Function to round down a number - see @here https://realpython.com/python-rounding/#rounding-down
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

# Do the calculations and return the correct amount of fuel
def solve(masses):
    totalFuel = 0
    for mass in masses:
        totalFuel = totalFuel + (round_down(mass / 3, 0) - 2)
    return totalFuel