import random

from apps.algorithms.mean import Mean
from apps.algorithms.standart_deviation import StandartDeviation
from apps.algorithms.z_value import ZValue
from apps.datasets.dataset import DataSet


__author__ = 'cenk'


def demo2():
    data_list = []
    value_size = 10000
    val = 0
    while val < value_size:
        data_list.append(random.randint(0, 1000000000))
        val += 1
    ## I add here anomly
    data_list.append(999999999999999999)
    random.shuffle(data_list)
    dataset = DataSet()
    dataset.set(data_list)
    train, validation, test = dataset.split_train_validation_test_data()
    training_list = train.get()
    validation_list = validation.get()
    test_list = test.get()
    standart_deviation = StandartDeviation()
    standart_deviation_value = standart_deviation.calculate(training_list)
    mean = Mean()
    mean_value = mean.calculate(training_list)
    # print "Training Set: %s, Validation Set: %s, Test Set: %s" % (training_list, validation_list, test_list)
    print "Standart Deviation: %f, Mean Value: %f" % (standart_deviation_value, mean_value)
    z_value = ZValue()
    counter = 0
    for val in validation_list:
        z_value.calculate(val, mean=mean_value, standart_deviation=standart_deviation_value)
        table_value = z_value.find_from_table()
        if table_value == -1:
            print "This val is anomaly:", val
            counter += 1
    print "Anomaly Count: %d, Dataset Count: %d" % (counter, dataset.__len__())
    counter = 0
    for val in test_list:
        z_value.calculate(val, mean=mean_value, standart_deviation=standart_deviation_value)
        table_value = z_value.find_from_table()
        if table_value == -1:
            print "This val is anomaly:", val
            counter += 1
    print "Anomaly Count: %d, Dataset Count: %d" % (counter, dataset.__len__())


if __name__ == "__main__":
    print "-*-" * 20, "Demo 2 Starts", "-*-" * 20
    demo2()
    print "-*-" * 20, "Demo 2 Ends", "-*-" * 20