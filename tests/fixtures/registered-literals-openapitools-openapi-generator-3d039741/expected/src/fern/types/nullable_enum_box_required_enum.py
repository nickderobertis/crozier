

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NullableEnumBoxRequiredEnum(enum.StrEnum):
    AUTO = "auto"
    LOW = "low"

    def visit(self, auto: typing.Callable[[], T_Result], low: typing.Callable[[], T_Result]) -> T_Result:
        if self is NullableEnumBoxRequiredEnum.AUTO:
            return auto()
        if self is NullableEnumBoxRequiredEnum.LOW:
            return low()
