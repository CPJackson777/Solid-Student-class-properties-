# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.


class Student:
    def __init__(self, first_name, last_name, age, cohort):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__cohort = cohort
    
    #getters for all properties
    @property 
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def age(self):
        return self.__age

    @property
    def cohort(self):
        return self.__cohort



    
