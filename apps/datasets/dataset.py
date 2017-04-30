import random
import operator

__author__ = 'cenk'


class DataSet:
    def __init__(self):
        self._data = None

    def __len__(self):
        return len(self._data)

    def set(self, data, extend=False):
        """
        Sets data to the dataset

        :param data: a list of tuples
        :type data: list
        """
        if extend:
            self._data.extend(data)
        else:
            self._data = data

    def get(self):
        """
        :returns: a list of tuples
        """
        return self._data

    def split_train_validation_test_data(self, percent=(60, 20, 20), shuffle_data=True):
        if self._data[0] is tuple:
            self._data = sorted(self._data, key=operator.itemgetter(1))
        else:
            self._data = sorted(self._data)
        length = len(self._data)
        first_5 = self._data[:int(round(length * 5 / 100.0))]
        last_5 = self._data[-int(round(length * 5 / 100.0)):]
        other = self._data[int(round(length * 5 / 100.0)) + 1:-int(round(length * 5 / 100.0))]
        if shuffle_data:
            random.shuffle(other)
        self._data = first_5 + other + last_5
        train_list = self._data[:int(round(length * percent[0] / 100.0))]
        validation_list = self._data[
                          int(round(length * percent[0] / 100.0)):int(
                              round(length * (percent[0] + percent[1]) / 100.0))]
        test_list = self._data[-int(round(length * ( percent[2]) / 100.0)):]
        # if self._data[0] is tuple:
        # self._data = sorted(self._data, key=operator.itemgetter(1))
        # else:
        # self._data = sorted(self._data)
        # n = len(self._data)
        # percent1 = percent[1]
        # percent2 = int(percent[2])
        # test_percent = (n * (percent2 / 2) / 100)
        # test_list = self._data[:test_percent] + self._data[-test_percent:]
        # validation_percent = (n * (percent2 + percent1 / 2) / 100)
        # validation_list = self._data[test_percent:validation_percent - 1] + self._data[
        # -validation_percent + 1:-test_percent]
        # train_list = self._data[validation_percent - 1:-validation_percent + 1]

        train = DataSet()
        train.set(train_list)
        validation = DataSet()
        validation.set(validation_list)
        test = DataSet()
        test.set(test_list)

        return train, validation, test