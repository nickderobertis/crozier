

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertEndPositionPropertiesType(enum.StrEnum):
    ESTIMATED = "Estimated"
    ACQUIRE = "Acquire"

    def visit(self, estimated: typing.Callable[[], T_Result], acquire: typing.Callable[[], T_Result]) -> T_Result:
        if self is AlertEndPositionPropertiesType.ESTIMATED:
            return estimated()
        if self is AlertEndPositionPropertiesType.ACQUIRE:
            return acquire()
