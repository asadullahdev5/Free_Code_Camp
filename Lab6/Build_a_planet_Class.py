# Build a Planet Class
# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should create a class named Planet.
# The Planet class should have an __init__ method that:
# Has four parameters: self, name, planet_type, and star.
# Raises a TypeError with the message name, planet type, and star must be strings if any of the arguments passed in is not a string type.
# Raises a ValueError with the message name, planet_type, and star must be non-empty strings if any of the arguments passed in is an empty string.
# Assigns the values passed in to the instance attributes name, planet_type, and star.
# The Planet class should have an orbit method that returns a string in the format {name} is orbiting around {star}....
# The Planet class should have a __str__ method that returns a string in the format Planet: {name} | Type: {planet_type} | Star: {star}.
# You should create three instances of the Planet class named planet_1, planet_2, and planet_3.
# You should print each planet object to see the __str__ method output.
# You should call the orbit method on each planet object and print the result.



class Planet:
    def __init__(self, name, planet_type, star):
        # Validate data types (Tests 4, 5, 6)
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError("name, planet type, and star must be strings")
            
        # Validate non-empty strings (Tests 7, 8, 9)
        if name == "" or planet_type == "" or star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")
            
        # Assign instance attributes (Tests 10, 11, 12)
        self.name = name
        self.planet_type = planet_type
        self.star = star

    # Orbit method (Tests 13, 14)
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    # String representation method (Tests 15, 16)
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


# Create three distinct instances (Test 17)
planet_1 = Planet("Earth", "Terrestrial", "The Sun")
planet_2 = Planet("Mars", "Terrestrial", "The Sun")
planet_3 = Planet("Jupiter", "Gas Giant", "The Sun")

# Print each object to trigger __str__ (Test 18)
print(planet_1)
print(planet_2)
print(planet_3)

# Call orbit on each and print the result (Test 19)
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
