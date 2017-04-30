import random
from datetime import datetime, timedelta

from apps.random.randoms import Randoms
from utils.logger import Logger


__author__ = 'cenk'


class MockData(Logger):
    def default_data(self, *args, **kwargs):
        interface = Randoms.random_from_list(['a', 'b', 'c'])
        sleep_time = random.randint(1, 10)
        data = {}
        start_date = datetime.now()
        end_date = datetime.now() + timedelta(seconds=sleep_time)
        data['temos'] = interface
        data['value'] = int(Randoms.random_with_probability() * sleep_time)
        data['start_date'] = start_date.strftime("%Y-%m-%d %H:%M %S")
        data['end_date'] = end_date.strftime("%Y-%m-%d %H:%M %S")
        data['time_delta'] = 1
        self.log(data)
        return data
