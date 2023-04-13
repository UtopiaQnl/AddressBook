import abc
from typing import TypeVar, Generic

from supportive.State import State

T = TypeVar("T")


class Controller(abc.ABC, Generic[T]):
    __slots__ = ("state", "__data")
    state: State
    __data: T

    def __init__(self, state: State, data: T) -> None:
        self.state = state
        self.data = data

    @property
    def data(self) -> T:
        return self.__data

    @data.setter
    def data(self, new_data: T) -> None:
        self.__data = new_data

    @abc.abstractmethod
    def run(self) -> State:
        raise NotImplemented
