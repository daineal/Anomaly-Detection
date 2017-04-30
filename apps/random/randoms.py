import random

__author__ = 'cenk'


class Randoms:
    @staticmethod
    def random(*args, **kwargs):
        range_1 = kwargs['range1'] if 'range1' in kwargs else (1000, 10000000)
        return random.randint(range_1[0], range_1[1])

    @staticmethod
    def random_with_probability(*args, **kwargs):
        required_percent = kwargs['probability'] if 'probability' in kwargs else None
        range_1 = kwargs['range1'] if 'range1' in kwargs else (1000, 10000000)  # 1000, 10000000
        range_2 = kwargs['range2'] if 'range2' in kwargs else (0, 1000)  # 0, 1000

        if not required_percent:
            return random.randint(range_1[0], range_1[1])

        percent = random.random()
        if percent < required_percent:
            return random.randint(range_2[0], range_2[1])

        return random.randint(range_1[0], range_1[1])

    @staticmethod
    def random_from_list(string_list, *args, **kwargs):
        return random.choice(string_list)
