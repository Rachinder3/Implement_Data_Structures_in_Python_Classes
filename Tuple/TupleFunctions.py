# importing the logging class
from logger.logger import Logger


class TupleClass:
    __log_obj = Logger(filename='logs//tupleLog.log')

    def __init__(self, t):

        """
        constructor of the class
        """

        temp = []  # doing deep copy and avoiding the shallow copy.
        for element in t:
            temp.append(element)
        self.__t = tuple(temp)

        self.__check_tuple()
        TupleClass.__log_obj.add_log(message='Initialized the Tuple')

    def __check_tuple(self):
        if type(self.__t) != tuple:
            raise Exception("Input is not a tuple. Please enter a Tuple")

    def __str__(self):
        return "Your tuple is: {}".format(self.__t)

    def count(self, value):
        """description: returns the count of given value
        """
        try:
            TupleClass.__log_obj.add_log(message="count function called")
            return self.__t.count(value)
        except Exception as e:
            TupleClass.__log_obj.add_log(message='Error occurred', mode='error')
            TupleClass.__log_obj.add_log(message=str(e), mode='error')

    def index(self, value):
        """description: returns the first index of value
        """
        try:
            TupleClass.__log_obj.add_log(message="index function called")
            return self.__t.index(value)
        except Exception as e:
            TupleClass.__log_obj.add_log(message='Error occurred', mode='error')
            TupleClass.__log_obj.add_log(message=str(e), mode='error')

    def __add__(self, other):
        """ description: overloads + operator
        """
        try:
            TupleClass.__log_obj.add_log(message="+ operator called")
            temp = self.__t + other.__t
            return TupleClass(temp)
        except Exception as e:
            TupleClass.__log_obj.add_log(message='Error occurred', mode='error')
            TupleClass.__log_obj.add_log(message=str(e), mode='error')

    def __mul__(self, multiplier):
        """description: overloads * operator
        """
        try:
            TupleClass.__log_obj.add_log(message="* operator called")
            return TupleClass(self.__t * multiplier)
        except Exception as e:
            TupleClass.__log_obj.add_log(message='Error occurred', mode='error')
            TupleClass.__log_obj.add_log(message=str(e), mode='error')