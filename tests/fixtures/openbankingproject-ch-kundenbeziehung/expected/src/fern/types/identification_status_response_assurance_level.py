

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdentificationStatusResponseAssuranceLevel(enum.StrEnum):
    LOW = "low"
    SUBSTANTIAL = "substantial"
    HIGH = "high"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        substantial: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentificationStatusResponseAssuranceLevel.LOW:
            return low()
        if self is IdentificationStatusResponseAssuranceLevel.SUBSTANTIAL:
            return substantial()
        if self is IdentificationStatusResponseAssuranceLevel.HIGH:
            return high()
