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

    #full name coded as a read-only string
    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'

#setters for all except the read-only properties
    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError("This should be a written name.")

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError("This should be a written name.")

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("This should be a number.")
    
    @cohort.setter
    def cohort(self, new_cohort):
        if type(new_cohort) is str:
            self.__cohort = new_cohort
        else:
            raise TypeError("This should be a written as 'Cohort' followed by the cohort number.")
    

charles = Student("Charles", "Jackson", 0, "cohort 36")

print(charles.full_name)


    
