# Making a class to represent an employee in a company. Each employee has a name, level, and salary. The salary is determined by the level of the employee.

class Employee:
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }
    # For the Employee class, we will define the following attributes:

    def __init__(self, name, level):
        if not (isinstance(name, str) and isinstance(level, str)):
            raise TypeError("'name' and 'level' attribute must be of type 'str'.")
        if level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")
        self._name = name
        self._level = level
        self._salary = Employee._base_salaries[level]

 # we will define the following methods for the Employee class:

    def __str__(self):
        return f'{self.name}: {self.level}'

    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"

    # property methods to access the attributes of the Employee class:
    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def salary(self):
        return self._salary
        
charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)

print (f"Base Salary: ${charlie_brown.salary}")

   