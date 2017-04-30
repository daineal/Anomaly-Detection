from unittest import TestCase

from apps.datasets.dataset import DataSet


__author__ = 'cenk'


class DataSetTest(TestCase):
    def test_split_train_validation_test_data(self):
        dataset = DataSet()
        dataset.set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        train, validation, test = dataset.split_train_validation_test_data()
        print train.get(), validation.get(), test.get()