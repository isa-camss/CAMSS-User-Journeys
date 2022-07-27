""" Script containing the class with support methods for other classes """
import os
from datetime import datetime


class UsefulMethods(object):
    """ Class that contains utility methods as a complement to other functions """

    @staticmethod
    def now() -> datetime:
        return datetime.now()
