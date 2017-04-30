from apps.algorithms.mean import Mean
from apps.algorithms.standart_deviation import StandartDeviation
from apps.algorithms.z_value import ZValue
from apps.csv.read_csv import ReadCsv
from apps.data_operations.create_data import CreateData
from apps.datasets.dataset import DataSet
import settings


__author__ = 'cenk'


def main():
    # write_klass = CreateData(**{'log_active': settings.LOG, 'limit': settings.LIMIT})
    # write_klass.start()
    for interface_name in settings.INTERFACE_NAMES:
        print "Interface Name: %s" % interface_name
        klass = ReadCsv(**{'log_active': False, 'interface_name': interface_name})
        klass.start()
        data, name = klass.get_data()
        dataset = DataSet()
        dataset.set(eval(data.get(name)))
        if dataset.__len__() <= 1:
            return
        train, validation, test = dataset.split_train_validation_test_data()
        training_list = train.get()
        validation_list = validation.get()
        test_list = test.get()
        if train.__len__() <= 1:
            return
        standart_deviation = StandartDeviation()
        standart_deviation_value = standart_deviation.calculate(training_list, is_tuple=True, index=1)
        mean = Mean()
        mean_value = mean.calculate(training_list, is_tuple=True, index=1)
        print "Standart Deviation: %f, Mean Value: %f" % (standart_deviation_value, mean_value)
        z_value = ZValue()
        counter = 0
        for val in validation_list:
            z_value.calculate(val, mean=mean_value, standart_deviation=standart_deviation_value, is_tuple=True, index=1)
            table_value = z_value.find_from_table()
            if table_value == -1:
                print "This val is anomaly:", val
                counter += 1
        print "Anomaly Count: %d, Dataset Count: %d" % (counter, dataset.__len__())
        counter = 0
        for val in test_list:
            z_value.calculate(val, mean=mean_value, standart_deviation=standart_deviation_value, is_tuple=True, index=1)
            table_value = z_value.find_from_table()
            if table_value == -1:
                print "This val is anomaly:", val
                counter += 1
        print "Anomaly Count: %d, Dataset Count: %d" % (counter, dataset.__len__())


if __name__ == "__main__":
    main()