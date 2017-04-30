import os

__author__ = 'cenk'

BASE_PATH = os.path.dirname(__file__)

DATA_PATH = os.path.join(BASE_PATH, '../data/data_test.csv')
Z_TABLE_PATH = os.path.join(BASE_PATH, '../data/z_table.csv')
LOG = False

LIMIT = 3000000
SLEEP_TIME = 0

CSV_HEADER = ['temos', 'start_date', 'end_date', 'time_delta', 'value']

USE_REDIS = False

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

INTERFACE_NAME = "a"
INTERFACE_NAMES = ["a", "b", "c"]

