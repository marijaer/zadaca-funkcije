import random

countries_cities = {"Austria": "Vienna",
                    "Croatia": "Zagreb",
                    "Spain": "Madrid",
                    "Slovenia": "Ljubljana",
                    "Hungary": "Budapest",
                    "France": "Paris",
                    "Germany": "Berlin"
                    }

countries = list(countries_cities.keys())

print("Welcome to the ultimate geography quizz. You will be asked to guess four capitals of European countries.")

point = 0

for country in random.sample(countries, 4):
    capital = countries_cities[country]
    guess = input("What is the capital of {}?" .format(country))

    if guess.capitalize() == capital:
        point += 1
        print("Correct, you receive 1 point")

    else:
        print("Wrong. The capital of {} is {}." .format(country, capital))

print("You are done. Your score is {} out of 4." .format(point))
