

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadFeederStrategy(enum.StrEnum):
    """
    how a row is chosen each iteration: CIRCULAR (default) cycles rows[globalIteration % size] and never exhausts; RANDOM picks a uniformly random row each iteration; SEQUENTIAL uses rows[globalIteration] once each in order and COMPLETES the run once the dataset is exhausted (data-driven replay-once).
    """

    CIRCULAR = "CIRCULAR"
    RANDOM = "RANDOM"
    SEQUENTIAL = "SEQUENTIAL"

    def visit(
        self,
        circular: typing.Callable[[], T_Result],
        random: typing.Callable[[], T_Result],
        sequential: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoadFeederStrategy.CIRCULAR:
            return circular()
        if self is LoadFeederStrategy.RANDOM:
            return random()
        if self is LoadFeederStrategy.SEQUENTIAL:
            return sequential()
