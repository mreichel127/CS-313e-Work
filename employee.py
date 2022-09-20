#  File: employee.py
#  Description: created an Employee class with specialized subclasses
#  Student Name: Madeline Reichel
#  Student UT EID: mr57723
#  Partner Name: Jennifer Kim
#  Partner UT EID: ck27924
#  Course Name: CS 313 E
#  Unique Number: 52520
#  Date Created: 09/06/2022
#  Date Last Modified: 09/12/2022

import sys
from unicodedata import name

class Employee:

    def __init__(self, **kwargs): # initializer 
        self.name = kwargs["name"] # setting kwargs to instance vars
        self.id = kwargs["id"]
        self.salary = None
        if "salary" in kwargs:
            self.salary = kwargs["salary"]
        self.title = "Employee"
        
    def __str__(self): # to string
        return self.title + "\n" + self.name + ", " + self.id + ", " + str(self.salary)


############################################################
############################################################
############################################################

class Permanent_Employee(Employee):

    def __init__(self, **kwargs): # initializer 
        super().__init__(**kwargs) # call to super initializer
        self.benefits = kwargs["benefits"]
        self.title = "Permanent_Employee"

    def cal_salary(self): # salary calculator
        if self.benefits == ["health_insurance"]:
            return self.salary * 0.9
        elif self.benefits == ["retirement"]:
            return self.salary * 0.8
        elif len(self.benefits) > 1:
            return self.salary * 0.7

    def __str__(self): # to string
        return super().__str__() + ", " + str(self.benefits)

############################################################
############################################################
############################################################

class Manager(Employee):
    def __init__(self, **kwargs): # initializer 
        super().__init__(**kwargs) # call to super initializer
        self.bonus = kwargs["bonus"]
        self.title = "Manager"

    def cal_salary(self): # salary calculator
        return self.salary + self.bonus

    def __str__(self): # to string
        return super().__str__() + ", " + str(self.bonus)


############################################################
############################################################
############################################################
class Temporary_Employee(Employee):
    def __init__(self, **kwargs): # initializer 
        super().__init__(**kwargs) # call to super initializer
        self.hours = kwargs["hours"]
        self.title = "Temporary_Employee"

    def cal_salary(self): # salary calculator
        return self.hours * self.salary

    def __str__(self): # to string
        return super().__str__() + ", " + str(self.hours)


############################################################
############################################################
############################################################


class Consultant(Temporary_Employee):

    def __init__(self, **kwargs): # initializer 
        super().__init__(**kwargs) # call to super initializer
        self.travel = kwargs["travel"]
        self.title = "Consultant"

    def cal_salary(self): # salary calculator
        return (1000 * self.travel) + super().cal_salary()

    def __str__(self): # to string
        return super().__str__() + ", " + str(self.travel)

############################################################
############################################################
############################################################


class Consultant_Manager(Consultant, Manager):
    def __init__(self,  **kwargs): # initializer 
        super().__init__(**kwargs) # call to super initializer
        self.title = "Consultant_Manager"

    def cal_salary(self): # salary calculator
        return super().cal_salary() + self.bonus

    def __str__(self): # to string
        return (f"{self.title}\n{self.name}, {self.id}, {self.salary}, {self.hours}, {self.travel}, Consultant_Manager\n{self.name}, {self.id}, {self.salary}, {self.bonus}")


############################################################
############################################################
############################################################



###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")


if __name__ == "__main__":
  main()
