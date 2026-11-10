

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateImageRequestModelOne(enum.StrEnum):
    DALL_E2 = "dall-e-2"
    DALL_E3 = "dall-e-3"

    def visit(self, dall_e2: typing.Callable[[], T_Result], dall_e3: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateImageRequestModelOne.DALL_E2:
            return dall_e2()
        if self is CreateImageRequestModelOne.DALL_E3:
            return dall_e3()
