import os

from apps.data_operations.create_data import CreateData
from settings import BASE_PATH


__author__ = 'cenk'


def create_demo_data(limit):
    path = os.path.join(BASE_PATH, '../data/demo' + str(limit) + '.csv')
    klass = CreateData(**{'log_active': False, 'limit': limit, 'path': path})
    klass.start()


if __name__ == "__main__":
    create_demo_data(3000)
    print 3000
    create_demo_data(30000)
    print 30000
    create_demo_data(300000)
    print 300000
    create_demo_data(3000000)
    print 3000000
    create_demo_data(12000000)
    print 12000000