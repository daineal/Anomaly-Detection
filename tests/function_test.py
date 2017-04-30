from unittest import TestCase
from datetime import datetime

from apps.algorithms.mean import Mean
from apps.algorithms.standart_deviation import StandartDeviation

from apps.algorithms.variance import Variance

from apps.csv.read_csv import ReadCsv
from apps.datasets.dataset import DataSet
import settings


__author__ = 'cenk'


class ImplementationTest(TestCase):
    def setUp(self):
        self.klass = ReadCsv(**{'log_active': settings.LOG})

    def test_dataset(self):
        dataset = DataSet()
        dataset.set(
            [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6), ('g', 7), ('h', 8), ('i', 9), ('j', 10)])

        training_set, validation_set, test_set = dataset.split_train_validation_test_data()
        print dataset.get()
        print len(training_set.get()), training_set.get()
        print len(validation_set.get()), validation_set.get()
        print len(test_set.get()), test_set.get()

        training_list = training_set.get()
        variance = Variance()
        variance_value = variance.calculate(training_list, is_tuple=True, index=1)
        standart_deviation = StandartDeviation()
        standart_deviation_value = standart_deviation.calculate(training_list, is_tuple=True, index=1)
        mean = Mean()
        mean_value = mean.calculate(training_list, is_tuple=True, index=1)
        print "Variance: %f" % variance_value
        print "Standart Deviation: %f" % standart_deviation_value
        print "Mean: %f" % mean_value

        print "*" * 10, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Finish Test", "*" * 10

    def test_create_dataset(self):
        self.klass.start()
        data, name = self.klass.get_data()
        dataset = DataSet()
        dataset.set(eval(data.get(name)))

        training_set, validation_set, test_set = dataset.split_train_validation_test_data()
        print dataset.get()
        print len(training_set.get()), training_set.get()
        print len(validation_set.get()), validation_set.get()
        print len(test_set.get()), test_set.get()

        training_list = training_set.get()
        variance = Variance()
        variance_value = variance.calculate(training_list, is_tuple=True, index=1)
        mean = Mean()
        mean_value = mean.calculate(training_list, is_tuple=True, index=1)
        print "Variance: %f" % variance_value
        print "Mean: %f" % mean_value

        print "*" * 10, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "Finish Test", "*" * 10
