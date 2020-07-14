<<<<<<< HEAD
from abc import ABC, abstractmethod  # to make a class abstract we need this import


class InvalidOperationError(Exception):
    pass


class Stream(ABC):             # when a class inherit from ABC it becomes abstract class
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("The stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("The stream is already closed.")
        self.opened = False

    @abstractmethod             #when we add a abstract decorator to a fuction it need to be defined in the class where it is to be inheritered
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading a data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data form a network.")



# A abstract class is a half baked cookie so we can use that class to create an object
# abstract class contain only the code the can be reused in many classes
=======
from abc import ABC, abstractmethod  # to make a class abstract we need this import


class InvalidOperationError(Exception):
    pass


class Stream(ABC):             # when a class inherit from ABC it becomes abstract class
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("The stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("The stream is already closed.")
        self.opened = False

    @abstractmethod             #when we add a abstract decorator to a fuction it need to be defined in the class where it is to be inheritered
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading a data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data form a network.")



# A abstract class is a half baked cookie so we can use that class to create an object
# abstract class contain only the code the can be reused in many classes
>>>>>>> 0356b09e8b6a933353bbc247cd08803d23fbd014
# abstractmethod decorator is used to make a function defined in the class where it is inherited