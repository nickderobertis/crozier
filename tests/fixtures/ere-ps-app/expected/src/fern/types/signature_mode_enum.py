

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SignatureModeEnum(enum.StrEnum):
    PIN = "PIN"
    COMFORT = "COMFORT"

    def visit(self, pin: typing.Callable[[], T_Result], comfort: typing.Callable[[], T_Result]) -> T_Result:
        if self is SignatureModeEnum.PIN:
            return pin()
        if self is SignatureModeEnum.COMFORT:
            return comfort()
