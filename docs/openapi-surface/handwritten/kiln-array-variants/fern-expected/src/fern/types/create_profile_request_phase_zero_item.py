

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateProfileRequestPhaseZeroItem(enum.StrEnum):
    HEATING = "heating"
    SOAKING = "soaking"

    def visit(self, heating: typing.Callable[[], T_Result], soaking: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateProfileRequestPhaseZeroItem.HEATING:
            return heating()
        if self is CreateProfileRequestPhaseZeroItem.SOAKING:
            return soaking()
