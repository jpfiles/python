# Create an instance of the MovieInfo class called new_movie. 
# Then, assign new_movie's attributes director and year with 
# the two values read from input, respectively.

# Ex: If the input is:
# Kim Carr
# 2006
# then the output is:

# Movie info: directed by Kim Carr, released 2006
class MovieInfo:
    def __init__(self):
        self.director = 'unknown'
        self.year = 0

director_in = input()
year_in = int(input())

new_movie = MovieInfo()
new_movie.director = director_in
new_movie.year = year_in

print('Movie info:', end=' ')
print(f'directed by {new_movie.director},', end=' ')
print(f'released {new_movie.year}')



# Output 'Windows: ' followed by the num_windows attribute of the HouseDetails object new_house.

# Ex: If the input is 34, then the output is:
# Windows: 34
class HouseDetails:
    def __init__(self):
        self.num_windows = 0

new_house = HouseDetails()
new_house.num_windows = int(input())

print(f'Windows: {new_house.num_windows}')


# The Rectangle class contains two attributes: length and width. Rectangle object rect1 is created with the length and width attributes read from input. 
# Given that total_perimiter = 2 * (length + width)
# use rect1's attributes, length and width, to calculate total_perimeter and assign the result to variable total_perimeter.

# Ex: If the input is:
# 11
# 7
# then the output is:
# Total perimeter: 36
class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

rect1 = Rectangle()
rect1.length = int(input())
rect1.width = int(input())

total_perimeter = 2 * (rect1.length + rect1.width)

print(f'Total perimeter: {total_perimeter}')


# Define a class named HouseData that contains the attributes num_doors and owner_name. Initialize num_doors with 0 and initialize owner_name with 'unknown'.

# Ex: If the input is:
# 19
# Gus Bell
# then the output is:
# House data (before): 0 doors, owned by unknown
# House data (after): 19 doors, owned by Gus Bell

class HouseData:
    def __init__(self):
        self.num_doors = 0
        self.owner_name = 'unknown'

house = HouseData()

print('House data (before):', end=' ')
print(f'{house.num_doors} doors,', end=' ')
print(f'owned by {house.owner_name}')

house.num_doors = int(input())
house.owner_name = input()

print('House data (after):', end=' ')
print(f'{house.num_doors} doors,', end=' ')
print(f'owned by {house.owner_name}')

# Add a method calculate_pay() to the Employee class. The method should return the amount to pay the employee by multiplying the employee's wage and number of hours worked.
class Employee:
    def __init__(self):
        self.wage = 0
        self.hours_worked = 0

    def calculate_pay(self):
        return self.wage * self.hours_worked

alice = Employee()
alice.wage = 9.25
alice.hours_worked = 35
print(f'Alice:\n Net pay: {alice.calculate_pay():.2f}')

barbara = Employee()
barbara.wage = 11.50
barbara.hours_worked = 20
print(f'Barbara:\n Net pay: {barbara.calculate_pay():.2f}')



# The following class represents a vehicle for sale in a used-car lot. Add a __str__() method so that printing an instance of Car displays a string in the following format:

# 1989 Chevrolet Blazer:
#   Mileage: 115000
#   Sticker price: $3250
class Car:
    def __init__(self, make, model, year, miles, price):
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles
        self.price = price

    def __str__(self):
        return (f'{self.year} {self.model}\n'
                f'Mileage: {self.miles}\n'
                f'Sticker price: {self.price}')

cars = []
cars.append(Car('Ford', 'Mustang', 2013, 25000, 37999))
cars.append(Car('Nissan', 'Xterra', 2004, 89500, 7500))
cars.append(Car('Nissan', 'Maxima', 2012, 25000, 15750))

for car in cars:
    print(car)

