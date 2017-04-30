# coding=utf-8
from utils.z_table import ZTable

__author__ = 'cenk'

"""
    Z = (X − μ) / σ
"""


class ZValue:
    def __init__(self):
        self._data = []
        self._z_value = None

    def calculate(self, data, mean, standart_deviation, is_tuple=False, index=None):
        if is_tuple:
            self._data = data[index]
        else:
            self._data = data
        self.standart_deviation = standart_deviation
        self.mean = mean
        return self.__algorithm()


    def __algorithm(self):
        self._z_value = round((float(self._data) - float(self.mean)) / float(self.standart_deviation), 2)
        return self._z_value

    def find_from_table(self):
        return ZTable().get_value(abs(self._z_value))