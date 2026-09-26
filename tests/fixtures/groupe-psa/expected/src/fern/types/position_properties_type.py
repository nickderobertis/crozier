

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PositionPropertiesType(enum.StrEnum):
    ESTIMATED = "Estimated"
    ACQUIRE = "Acquire"

    def visit(self, estimated: typing.Callable[[], T_Result], acquire: typing.Callable[[], T_Result]) -> T_Result:
        if self is PositionPropertiesType.ESTIMATED:
            return estimated()
        if self is PositionPropertiesType.ACQUIRE:
            return acquire()
