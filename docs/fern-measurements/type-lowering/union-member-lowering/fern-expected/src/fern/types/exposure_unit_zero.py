

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExposureUnitZero(enum.StrEnum):
    SECONDS = "seconds"

    def visit(self, seconds: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExposureUnitZero.SECONDS:
            return seconds()
