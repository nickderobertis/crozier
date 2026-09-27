

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExpectationResponseMode(enum.StrEnum):
    SEQUENTIAL = "SEQUENTIAL"
    RANDOM = "RANDOM"
    WEIGHTED = "WEIGHTED"
    SWITCH = "SWITCH"

    def visit(
        self,
        sequential: typing.Callable[[], T_Result],
        random: typing.Callable[[], T_Result],
        weighted: typing.Callable[[], T_Result],
        switch: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExpectationResponseMode.SEQUENTIAL:
            return sequential()
        if self is ExpectationResponseMode.RANDOM:
            return random()
        if self is ExpectationResponseMode.WEIGHTED:
            return weighted()
        if self is ExpectationResponseMode.SWITCH:
            return switch()
