from abc import abstractmethod


class Sequence:
    def __init__(self, items):
        self.items = items
        pass

    def __len__(self):
        pass

    @abstractmethod
    def iter_seq(self):
        """
        Static operation
        :return:
        """

    @abstractmethod
    def get_at(self, i):
        """
        Static operation
        :param i:
        :return:
        """

    @abstractmethod
    def set_at(self, i, x):
        """
        Static Operation
        :param i:
        :param x:
        :return:
        """

    @abstractmethod
    def insert_at(self, i, x):
        """
        Dynamic operation
        :param i:
        :param x:
        :return:
        """

    @abstractmethod
    def delete_at(self, i):
        """
        Dynamic operation
        :param i:
        :return:
        """

    @abstractmethod
    def insert_first(self, x):
        """
        Dynamic operation
        :param x:
        :return:
        """

    @abstractmethod
    def delete_first(self):
        """
        Dynamic operation
        :return:
        """

    @abstractmethod
    def insert_last(self, x):
        """
        Dynamic operation
        :param x:
        :return:
        """

    @abstractmethod
    def delete_last(self):
        """
        Dynamic operation
        :return:
        """

