

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExposureUnitOne(enum.StrEnum):
    MILLISECONDS = "milliseconds"

    def visit(self, milliseconds: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExposureUnitOne.MILLISECONDS:
            return milliseconds()
