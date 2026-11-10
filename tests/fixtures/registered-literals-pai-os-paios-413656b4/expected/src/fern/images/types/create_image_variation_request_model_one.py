

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateImageVariationRequestModelOne(enum.StrEnum):
    DALL_E2 = "dall-e-2"

    def visit(self, dall_e2: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateImageVariationRequestModelOne.DALL_E2:
            return dall_e2()
