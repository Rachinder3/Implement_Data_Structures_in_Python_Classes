from logger.logger import Logger


class DictionaryClass():
    __log_obj = Logger("logs//dictionaryLog.log")  # making class variable. For  each object we don't need separate log

    # object. Hence, this is a class variable.

    def __init__(self, d):
        """constructor of the class
        """

        self.__d = {}

        for key in d:  # doing deep copy
            self.__d[key] = d[key]

        self.__check_dict()

        DictionaryClass.__log_obj.add_log(message="Dictionary initialized")

    def __check_dict(self):
        """method to check if input is correct
        """
        if type(self.__d) != dict:
            raise Exception("Input is not a dictionary. Please enter a dictionary. ")

    def __str__(self):
        """description: overloads the print function
        """
        DictionaryClass.__log_obj.add_log(message="Print function is called")
        return "Your dictionary is: {}".format(self.__d)

    def clear(self):
        """description: clears the dictionary
        """
        try:
            DictionaryClass.__log_obj.add_log(message="clear function called")
            self.__d = {}
        except Exception as e:
            DictionaryClass.__log_obj.add_log(message='Error occurred', mode='error')
            DictionaryClass.__log_obj.add_log(message=str(e), mode='error')

    def copy(self):
        """description: creates and returns a copy of the dictionary object
        """
        try:
            DictionaryClass.__log_obj.add_log(message="copy function called")
            temp = DictionaryClass(self.__d)
            return temp
        except Exception as e:
            DictionaryClass.__log_obj.add_log(message='Error occurred', mode='error')
            DictionaryClass.__log_obj.add_log(message=str(e), mode='error')

    def fromkeys(self, iterable, value=None):
        """description: creates a dictionary from given iterable as key"""
        try:
            DictionaryClass.__log_obj.add_log(message="from keys method called")
            temp = {}
            for i in iterable:
                temp[i] = value
            return temp
        except Exception as e:
            DictionaryClass.__log_obj.add_log(message='Error occurred', mode='error')
            DictionaryClass.__log_obj.add_log(message=str(e), mode='error')

    def get(self, key, default=None):
        """description: returns value for the given key, else returns default"""
        try:
            DictionaryClass.__log_obj.add_log(message="get method called")

            try:
                return self.__d[key]
            except:
                return default

        except Exception as e:
            DictionaryClass.__log_obj.add_log(message='Error occurred', mode='error')
            DictionaryClass.__log_obj.add_log(message=str(e), mode='error')

    def items(self):
        """description: returns key, value pairs in the form of tuples"""

        try:
            DictionaryClass.__log_obj.add_log(message="items method called")

            return self.__d.items()

        except Exception as e:
            DictionaryClass.__log_obj.add_log(message='Error occurred', mode='error')
            DictionaryClass.__log_obj.add_log(message=str(e), mode='error')

    def keys(self):
        """description: returns keys of the dictionary object"""
        try:
            DictionaryClass.__log_obj.add_log(message="keys method called")
            return self.__d.keys()
        except Exception as e:
            DictionaryClass.__log_obj.add_log(message='Error occurred', mode='error')
            DictionaryClass.__log_obj.add_log(message=str(e), mode='error')

    def pop(self, key):
        """description: removes the corresponding key and returns the value"""

        try:
            DictionaryClass.__log_obj.add_log(message="pop method called")
            temp = self.__d.pop(key)

            return temp
        except Exception as e:
            DictionaryClass.__log_obj.add_log(message='Error occurred', mode='error')
            DictionaryClass.__log_obj.add_log(message=str(e), mode='error')

    def popitem(self):
        """
        description: removes and returns a (key, value) pair as 2 - tuple
        pairs returned in LIFO order
        """
        try:
            DictionaryClass.__log_obj.add_log(message="pop item method called")

            return self.__d.popitem()
        except Exception as e:
            DictionaryClass.__log_obj.add_log(message='Error occurred', mode='error')
            DictionaryClass.__log_obj.add_log(message=str(e), mode='error')

    def values(self):
        """description: returns the values in the dictionary"""

        try:
            DictionaryClass.__log_obj.add_log(message="values method called")

            return self.__d.values()
        except Exception as e:
            DictionaryClass.__log_obj.add_log(message='Error occurred', mode='error')
            DictionaryClass.__log_obj.add_log(message=str(e), mode='error')

    def setdefault(self, key, default=None):
        """ description: Insert key with a value of default if key is not in the dictionary.
        Return the value for key if key is in the dictionary, else default."""

        try:
            DictionaryClass.__log_obj.add_log(message="setdefault function called")

            return self.__d.setdefault(key, default)
        except Exception as e:
            DictionaryClass.__log_obj.add_log(message='Error occurred', mode='error')
            DictionaryClass.__log_obj.add_log(message=str(e), mode='error')
