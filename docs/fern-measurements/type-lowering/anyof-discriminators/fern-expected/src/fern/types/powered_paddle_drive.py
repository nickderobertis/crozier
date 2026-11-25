

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PoweredPaddleDrive(enum.StrEnum):
    POWERED = "powered"

    def visit(self, powered: typing.Callable[[], T_Result]) -> T_Result:
        if self is PoweredPaddleDrive.POWERED:
            return powered()
