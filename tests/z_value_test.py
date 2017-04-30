from unittest import TestCase

from apps.algorithms.mean import Mean
from apps.algorithms.standart_deviation import StandartDeviation
from apps.algorithms.z_value import ZValue


__author__ = 'cenk'


class ZValueTest(TestCase):
    def setUp(self):
        pass

    def test_algorithm_with_list(self):
        data_list = [1, 2, 3, 4, 5]
        standart_deviation = StandartDeviation()
        standart_deviation_value = standart_deviation.calculate(data_list)
        mean = Mean()
        mean_value = mean.calculate(data_list)
        print standart_deviation_value, mean_value
        z_value = ZValue()
        z1 = z_value.calculate(88, mean=100, standart_deviation=10)
        z2 = z_value.calculate(112, mean=100, standart_deviation=10)
        z3 = z_value.calculate(5, mean=100, standart_deviation=10)
        print z1, z2, z3

    def test_get_decimals(self):
        z_value = ZValue()
        z_value.calculate(88, mean=100, standart_deviation=10)
        z_value.find_from_table()

    def test_algorithm_with_tuple(self):
        mean = Mean()
        data_list = [("a", 1), ("b", 2), ("c", 3), ( "d", 4), ("e", 5)]
        self.assertEquals(3, mean.calculate(data_list, is_tuple=True, index=1))

        data_list = [("a", "a", 1), ("b", "b", 2), ("c", "c", 3), ("d", "d", 4), ("e", "e", 5)]
        self.assertEquals(3.0, mean.calculate(data_list, is_tuple=True, index=2))