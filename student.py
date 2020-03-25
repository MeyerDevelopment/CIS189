"""
Program: student.py
Author: David Meyer
Last date modified: 03/24/2020
e-mail: dpmeyer@dmacc.edu


The purpose of this program is to run unit tests on a class
"""
class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa = 0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(major)):
            raise ValueError
        elif not isinstance(gpa, float):
            raise ValueError
        elif gpa > 4.0:
            raise ValueError
        elif gpa < 0.0:
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
