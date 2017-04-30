from unittest import TestCase

from apps.csv.read_csv import ReadCsv
from apps.datasets.dataset import DataSet
import settings


__author__ = 'cenk'


class ReadDataTest(TestCase):
    def setUp(self):
        self.klass = ReadCsv(**{'log_active': settings.LOG})

    def test_read_data_from_csv(self):
        self.klass.start()

    def test_get_data(self):
        self.klass.start()
        data, name = self.klass.get_data()
        dataset = DataSet()
        dataset.set(data.get(name))
        print dataset.get()

