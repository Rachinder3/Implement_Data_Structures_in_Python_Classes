from logger.logger import Logger


class SetClass():
    __log_obj = Logger("logs//SetLog.log")  # making class variable. For  each object we don't need separate log

    # object. Hence, this is a class variable.

    def __init__(self, s):
        """constructor of the class
        """

        self.__s = set()

        for key in s:  # doing deep copy and avoiding shallow copy
            self.__s.add(key)

        self.__check_set()

        SetClass.__log_obj.add_log(message="Set initialized")

    def __check_set(self):
        """method to check if input is correct
        """
        if type(self.__s) != set:
            raise Exception("Input is not a set. Please enter a set. ")

    def __str__(self):
        """description: overloads the print function
        """
        SetClass.__log_obj.add_log(message="Print function is called on ".format(self.__s))
        return "Your set is: {}".format(self.__s)

    def add(self, key):
        """description: adds a key into the set. If key is already present, nothing happens"""
        try:
            SetClass.__log_obj.add_log(message='add method called on '.format(self.__s))
            self.__s.add(key)

        except Exception as e:
            SetClass.__log_obj.add_log(message='Error occurred', mode='error')
            SetClass.__log_obj.add_log(message=str(e), mode='error')

    def clear(self):
        """description: clears the given set"""
        try:
            SetClass.__log_obj.add_log(message="clear method called on".format(self.__s))
            self.__s = set()

        except Exception as e:
            SetClass.__log_obj.add_log(message='Error occurred', mode='error')
            SetClass.__log_obj.add_log(message=str(e), mode='error')

    def copy(self):
        """description: creates a copy of the given object"""

        try:
            SetClass.__log_obj.add_log(message="copy method called on {}" .format(self.__s))
            temp = SetClass(self.__s)
            return temp

        except Exception as e:
            SetClass.__log_obj.add_log(message='Error occurred', mode='error')
            SetClass.__log_obj.add_log(message=str(e), mode='error')

    def difference(self, *args):
        """ description : returns the difference b/w the base set and given sets in args. Difference is those
        elements present in base set that are not present in other sets """
        try:
            SetClass.__log_obj.add_log("difference method called on {} ".format(self.__s))
            dif_set = self.__s
            for individual_set in args:
                dif_set = dif_set.difference(individual_set.__s)
            return SetClass(dif_set)
        except Exception as e:
            SetClass.__log_obj.add_log(message='Error occurred', mode='error')
            SetClass.__log_obj.add_log(message=str(e), mode='error')

    def difference_update(self, *args):
        """description: gets the difference b/w base set and given sets in args. Make changes inplace"""
        try:
            SetClass.__log_obj.add_log("difference update method called on {} ".format(self.__s))
            dif_set = self.__s
            for individual_set in args:
                dif_set = dif_set.difference(individual_set.__s)
            self.__s=dif_set
        except Exception as e:
            SetClass.__log_obj.add_log(message='Error occurred', mode='error')
            SetClass.__log_obj.add_log(message=str(e), mode='error')

    def discard(self, element):
        """description: removes an element from the set. If element not present, do nothing"""
        try:
            SetClass.__log_obj.add_log(message="discard method called on {}".format(self.__s))
            self.__s.discard(element)
        except Exception as e:
            SetClass.__log_obj.add_log(message='Error occurred', mode='error')
            SetClass.__log_obj.add_log(message=str(e), mode='error')

    def intersection(self, *args):
        """description: gets the intersection b/w base set and given set in args. """
        try:
            SetClass.__log_obj.add_log(message='intersection method called on {}'.format(self.__s))
            intersection_set=self.__s
            for individual_set in args:

                intersection_set=intersection_set.intersection(individual_set.__s)

            return SetClass(intersection_set)
        except Exception as e:
            SetClass.__log_obj.add_log(message='Error occurred', mode='error')
            SetClass.__log_obj.add_log(message=str(e), mode='error')

    def isDisjoint(self, set2):
        """description: returns True if 2 set objects have nothing in common"""
        try:
            SetClass.__log_obj.add_log(message='isDijoint method called on {} '.format(self.__s))
            return self.__s.isdisjoint(set2.__s)
        except Exception as e:
            SetClass.__log_obj.add_log(message='Error occurred', mode='error')
            SetClass.__log_obj.add_log(message=str(e), mode='error')


    def pop(self):
        """description: removes an arbitrary element in the set"""
        try:
            SetClass.__log_obj.add_log(message="pop method called on {} ".format(self.__s))
            self.__s.pop()
        except Exception as e:
            SetClass.__log_obj.add_log(message='Error occurred', mode='error')
            SetClass.__log_obj.add_log(message=str(e), mode='error')


    def remove(self, element):
        """description : removes a particular element from the set"""

        try:
            SetClass.__log_obj.add_log(message='remove method called on {}'.format(self.__s))
            self.__s.remove(element)
        except Exception as e:
            SetClass.__log_obj.add_log(message='Error occurred', mode='error')
            SetClass.__log_obj.add_log(message=str(e), mode='error')