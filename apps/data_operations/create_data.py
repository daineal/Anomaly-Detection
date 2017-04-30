from apps.csv.write_csv import WriteCsv


__author__ = 'cenk'


class CreateData(WriteCsv):
    def __init__(self, *args, **kwargs):
        super(CreateData, self).__init__(**kwargs)

