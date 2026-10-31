

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ComplexTypesWithCatchResponseResultDataStatus(enum.StrEnum):
    ON = "on"
    OFF = "off"

    def visit(self, on: typing.Callable[[], T_Result], off: typing.Callable[[], T_Result]) -> T_Result:
        if self is ComplexTypesWithCatchResponseResultDataStatus.ON:
            return on()
        if self is ComplexTypesWithCatchResponseResultDataStatus.OFF:
            return off()
