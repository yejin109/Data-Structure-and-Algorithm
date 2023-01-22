import os
import argparse

if __name__ == '__main__':
    os.chdir('..')
    print('Current Dir: ', os.getcwd())

from interface.sequence import Sequence
from utils.setup import load_data
from utils import log
import env


parser = argparse.ArgumentParser()
parser.add_argument('--size', default=1000, required=False)
parser.add_argument('--high', default=10000, required=False)
parser.add_argument('--low', default=0, required=False)

args = parser.parse_args()


class DynamicArraySequence(Sequence):
    def __init__(self):
        super().__init__(self)


class ArraySequence(Sequence):
    def __init__(self, items):
        super().__init__(self)
        self.items = [i for i in items]
        self.iters = iter(items)

    def __len__(self):
        return len(self.items)

    def iter_seq(self):
        next(self.iters)

    def get_at(self, i):
        return self.items[i]

    def set_at(self, i, x):
        self.items[i] = x

    def insert_at(self, i, x):
        self.items = self.items[:i] + [x] + self.items[i:]

    def delete_at(self, i):
        del self.items[i]

    def insert_first(self, x):
        self.items = [x] + self.items

    def delete_first(self):
        del self.items[0]

    def insert_last(self, x):
        self.items = self.items + [x]

    def delete_last(self):
        del self.items[len(self.items)]


def _array_seq_test(tsample):
    arr_seq = ArraySequence(tsample)
    log.print_attrs(arr_seq)
    log.print_methods(arr_seq)

    log.test_func(arr_seq.get_at, 0)
    log.test_func(arr_seq.set_at, 0, -1)
    log.test_func(arr_seq.get_at, 0)

    env.TEST_ITERATION = 1
    log.test_func(arr_seq.__len__)
    log.test_func(arr_seq.insert_at, 0, -1)
    log.test_func(arr_seq.__len__)

    log.test_func(arr_seq.__len__)
    log.test_func(arr_seq.delete_at, 0)
    log.test_func(arr_seq.__len__)


if __name__ == '__main__':
    # Array Sequencee Array
    data = load_data(**vars(args))
    _array_seq_test(data)
