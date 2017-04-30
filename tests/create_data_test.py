from unittest import TestCase

from apps.data_operations.create_data import CreateData
import settings


__author__ = 'cenk'


class CreateDataTest(TestCase):
    def test_write_data_to_csv(self):
        klass = CreateData(**{'log_active': settings.LOG, 'limit': settings.LIMIT})
        klass.start()
