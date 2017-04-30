import csv
import time

from apps.mocks.mock_data import MockData
from settings import DATA_PATH, CSV_HEADER, LIMIT, SLEEP_TIME
from utils.logger import Logger


__author__ = 'cenk'


class WriteCsv(Logger):
    def __init__(self, *args, **kwargs):
        super(WriteCsv, self).__init__(**kwargs)
        self.path = kwargs['path'] if 'path' in kwargs   else DATA_PATH
        self.header = kwargs['header'] if 'header' in kwargs   else CSV_HEADER
        self.limit = kwargs['limit'] if 'limit' in kwargs else LIMIT
        self.sleep_time = kwargs['sleep_time'] if 'sleep_time' in kwargs  else SLEEP_TIME
        self.data = kwargs['data'] if 'data' in kwargs  else MockData().default_data

    def start(self, *args, **kwargs):
        with open(self.path, 'wb') as csvfile:
            w = csv.DictWriter(csvfile, fieldnames=self.header)
            try:
                counter = 0
                while counter < self.limit:
                    data = self.data()
                    w.writerow(data)
                    counter += 1
                    self.log(data)
                    time.sleep(self.sleep_time)
            except:
                raise
        csvfile.close()