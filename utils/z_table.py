import csv

from settings import Z_TABLE_PATH


__author__ = 'cenk'


class ZTable:
    z_table = {}
    with open(Z_TABLE_PATH, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        column_names = None

        for row in spamreader:
            if column_names != None:
                for index, column in enumerate(column_names):
                    if index != 0:
                        key = float(row[0]) + float(column)
                        z_table[str(key)] = row[index]
            else:
                column_names = row
    csvfile.close()

    def get_value(self, index):
        try:
            return ZTable.z_table[str(index)]
        except:
            return -1