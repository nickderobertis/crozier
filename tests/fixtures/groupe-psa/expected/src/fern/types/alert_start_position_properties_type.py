

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertStartPositionPropertiesType(enum.StrEnum):
    ESTIMATED = "Estimated"
    ACQUIRE = "Acquire"

    def visit(self, estimated: typing.Callable[[], T_Result], acquire: typing.Callable[[], T_Result]) -> T_Result:
        if self is AlertStartPositionPropertiesType.ESTIMATED:
            return estimated()
        if self is AlertStartPositionPropertiesType.ACQUIRE:
            return acquire()
