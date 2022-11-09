'''
Program: overriding_class_methods.py
Author: Joshua M. McGinley
Last date modified: 11/09/2022

Using the Employee class from the encapsulation assignment in Module 10 - Topic 1, remove salaried, start_date and
salary from the constructor.  This is now the base class.
UML for assignment
Create two derived classes, SalariedEmployee and HourlyEmployee.
SalariedEmployee with members start_date and salary and methods give_raise() that updates salary and display() that
returns a string.
Include a driver that

    Creates a SalariedEmployee object (select a meaningful name) with your name, start date today, starting salary
    $40,000.

    Displays the Employee object
    Changes salary to $45,000
    Displays the Employee object

HourlyEmployee has hourly_pay, start_date, method give_raise() that updates salary and display() that returns a
string.
Include a driver that

    Creates a HourlyEmployee object (select a meaningful name) with your name, start date today, starting
    hourly_pay $10.00

    Displays the Employee object
    Changes hourly_pay to $12.00 an hour
    Displays the Employee object
'''

class Employee:
    def __init__(self, lname, fname):
        self.last_name = lname
        self.first_name = fname

class SalariedEmployee(Employee):
    def __init__(self, last_name, first_name, s_date, s_salary = 40000 ):
        super().__init__(last_name, first_name)
        self.start_date = s_date
        self.salary = s_salary

    def give_raise(self, new_salary):
        self.salary = new_salary

    def display(self):
        return self.first_name + ' ' + self.last_name + '\nStarted on: ' + self.start_date + '\n' + str(self.salary)

class HourlyEmployee(Employee):
    def __init__(self, last_name, first_name, s_date, h_pay = 10.00):
        super().__init__(last_name, first_name)
        self.start_date = s_date
        self.hourly_pay = h_pay

    def give_raise(self, new_pay):
        self.hourly_pay = new_pay

    def display(self):
        return self.first_name + ' ' + self.last_name + '\nStarted on: ' + self.start_date + '\n' + str(self.hourly_pay)


s_emp = SalariedEmployee('McGinley', 'Joshua', '11-9-2022')
print(s_emp.display())
s_emp.give_raise(45000)
print(s_emp.display())
h_emp = HourlyEmployee('McGinley', 'Joshua', '11-9-2022')
print(h_emp.display())
h_emp.give_raise(12.00)
print(h_emp.display())


