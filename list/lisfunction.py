# importing the logging class
from logger.logger import *


class ListClass:
    __log_obj = Logger('logs//listLog.log')  # making class variable. For  each object we don't need separate log

    # object. Hence, this is a class variable.

    def __init__(self, l):
        """
        constructor of the class
        """

        self.__l = []  # doing deep copy and avoiding shallow copy. If we directly do self.__l =l , it will just copy
        # the address and
        # won't create a new list.
        for i in l:  # iterating over the list.
            self.__l.append(i)

        self.__checkList()
        ListClass.__log_obj.add_log(message='Initialized the List', mode='info')

    def __checkList(self): # method to check if input is correct. It's a private method as this method is not needed
        # outside class
        if type(self.__l) != list:
            raise Exception("Input is not a list. Please enter a list")

    def __str__(self):
        """
        description: overloads the print function
        """
        ListClass.__log_obj.add_log(message='Print function called', mode='info')
        return "Your list is: {}".format(str(self.__l))

    def append(self, value):
        """
        description: implements the print function
        """
        try:
            self.__l.append(value)
            ListClass.__log_obj.add_log(message="append called on list {} ".format(self.__l), mode='info')
        except Exception as e:
            ListClass.__log_obj.add_log(message='Error occurred', mode='error')
            ListClass.__log_obj.add_log(message=str(e), mode='error')

    def clear(self):
        """
        description: clears the list
        """
        try:
            ListClass.__log_obj.add_log(message='clear function called', mode='info')
            self.__l = []
        except Exception as e:
            ListClass.__log_obj.add_log(message='Error occurred', mode='error')
            ListClass.__log_obj.add_log(message=str(e), mode='error')

    def copy(self):
        """
        description: returns copy of the list
        """
        try:
            ListClass.__log_obj.add_log(message='copy function called', mode='info')
            temp = ListClass(self.__l)
            return temp
        except Exception as e:
            ListClass.__log_obj.add_log(message='Error occurred', mode='error')
            ListClass.__log_obj.add_log(message=str(e), mode='error')

    def count(self, value):
        try:
            ListClass.__log_obj.add_log(message='Count function called', mode='info')
            return self.__l.count(value)
        except Exception as e:
            ListClass.__log_obj.add_log(message='Error occurred', mode='error')
            ListClass.__log_obj.add_log(message=str(e), mode='error')

    def extend(self, iterable):

        """
        description: Extends the List with given iterable. Unravels the iterable first and then appends
        """
        try:
            ListClass.__log_obj.add_log(message='Extend function called', mode='info')
            for element in iterable:
                self.__l.append(element)

        except Exception as e:
            ListClass.__log_obj.add_log(message='Error occurred', mode='error')
            ListClass.__log_obj.add_log(message=str(e), mode='error')

    def index(self, value):
        """
        description:Returns the first index of the given value in the list.
        """
        try:
            ListClass.__log_obj.add_log(message='index function called')
            for index, element in enumerate(self.__l):
                if element == value:
                    return index
            return -1  # element not found
        except Exception as e:
            ListClass.__log_obj.add_log(message='Error occurred', mode='error')
            ListClass.__log_obj.add_log(message=str(e), mode='error')

    def insert(self, index, element):
        """
        description: Adds the element in the list before the index.
        """
        try:
            ListClass.__log_obj.add_log(message='insert function called')
            self.__l.insert(index, element)
        except Exception as e:
            ListClass.__log_obj.add_log(message='Error occurred', mode='error')
            ListClass.__log_obj.add_log(message=str(e), mode='error')

    def pop(self, index=-1):
        """description: Removes the element at given index
        """
        try:
            ListClass.__log_obj.add_log("Pop function called")
            self.__l.pop(index)
        except Exception as e:
            ListClass.__log_obj.add_log(message='Error occurred', mode='error')
            ListClass.__log_obj.add_log(message=str(e), mode='error')

    def remove(self, value):
        """ description: Removes first occurrence of value.
        """
        try:
            ListClass.__log_obj.add_log("remove function called")
            self.__l.remove(value)
        except Exception as e:
            ListClass.__log_obj.add_log(message='Error occurred', mode='error')
            ListClass.__log_obj.add_log(message=str(e), mode='error')

    def reverse(self):
        """description: reverses the list in place
        """
        try:
            ListClass.__log_obj.add_log("reverse function called")
            self.__l.reverse()
        except Exception as e:
            ListClass.__log_obj.add_log(message='Error occurred', mode='error')
            ListClass.__log_obj.add_log(message=str(e), mode='error')

    def sort(self, reverse=False):
        """description: sorts the list in place in ascending order. Set reverse to True to sort in descending order.
        """
        try:
            ListClass.__log_obj.add_log("sort function called")
            self.__l.sort(reverse=reverse)
        except Exception as e:
            ListClass.__log_obj.add_log(message='Error occurred', mode='error')
            ListClass.__log_obj.add_log(message=str(e), mode='error')

    def __add__(self, other):
        """description: overloads the + operator.
        """
        try:
            ListClass.__log_obj.add_log("+ operator called")
            new_list = ListClass(self.__l+other.__l)
            return new_list
        except Exception as e:
            ListClass.__log_obj.add_log(message='Error occurred', mode='error')
            ListClass.__log_obj.add_log(message=str(e), mode='error')

    def __mul__(self, multiplier):
        """description: overloads the * operator.
        """
        try:
            ListClass.__log_obj.add_log("* operator called")
            newlist = ListClass(self.__l * multiplier)
            return newlist
        except Exception as e:
            ListClass.__log_obj.add_log(message='Error occurred', mode='error')
            ListClass.__log_obj.add_log(message=str(e), mode='error')

