

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExposureModeOne(enum.StrEnum):
    AUTOMATIC = "automatic"

    def visit(self, automatic: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExposureModeOne.AUTOMATIC:
            return automatic()
