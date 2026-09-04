

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FinancingType(enum.StrEnum):
    HARDWARE_FINANCING = "hardwareFinancing"
    BUSINESS_FINANCING = "businessFinancing"

    def visit(
        self, hardware_financing: typing.Callable[[], T_Result], business_financing: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is FinancingType.HARDWARE_FINANCING:
            return hardware_financing()
        if self is FinancingType.BUSINESS_FINANCING:
            return business_financing()
