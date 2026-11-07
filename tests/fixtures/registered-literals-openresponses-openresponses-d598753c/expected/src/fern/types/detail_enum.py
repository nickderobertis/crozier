

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetailEnum(enum.StrEnum):
    LOW = "low"
    HIGH = "high"
    AUTO = "auto"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DetailEnum.LOW:
            return low()
        if self is DetailEnum.HIGH:
            return high()
        if self is DetailEnum.AUTO:
            return auto()
