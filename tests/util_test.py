from unittest import TestCase

__author__ = 'cenk'


def util(data_set):
    percent = (60, 20, 20)
    n = len(data_set)
    percent0 = percent[0]
    percent1 = percent[1]
    percent2 = int(percent[2])
    test_percent = (n * (percent2 / 2) / 100)
    test = data_set[:test_percent] + data_set[-test_percent:]
    print test

    validation_percent = (n * (percent2 + percent1 / 2) / 100)

    validation = data_set[test_percent:validation_percent - 1] + data_set[-validation_percent + 1:-test_percent]
    print validation
    train = data_set[validation_percent - 1:-validation_percent + 1]
    print train
    pass


class UtilTest(TestCase):
    def test_util(self):
        data_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        util(data_set)