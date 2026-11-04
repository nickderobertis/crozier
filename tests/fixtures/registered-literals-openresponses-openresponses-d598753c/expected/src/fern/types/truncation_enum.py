

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TruncationEnum(enum.StrEnum):
    AUTO = "auto"
    DISABLED = "disabled"

    def visit(self, auto: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is TruncationEnum.AUTO:
            return auto()
        if self is TruncationEnum.DISABLED:
            return disabled()
