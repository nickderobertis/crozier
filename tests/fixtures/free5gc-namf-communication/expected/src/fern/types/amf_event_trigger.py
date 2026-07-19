

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AmfEventTrigger(enum.StrEnum):
    ONE_TIME = "ONE_TIME"
    CONTINUOUS = "CONTINUOUS"

    def visit(self, one_time: typing.Callable[[], T_Result], continuous: typing.Callable[[], T_Result]) -> T_Result:
        if self is AmfEventTrigger.ONE_TIME:
            return one_time()
        if self is AmfEventTrigger.CONTINUOUS:
            return continuous()
