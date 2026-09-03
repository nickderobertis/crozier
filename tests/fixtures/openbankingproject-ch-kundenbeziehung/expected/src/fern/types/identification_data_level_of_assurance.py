

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdentificationDataLevelOfAssurance(enum.StrEnum):
    """
    Sicherheitsniveau (eIDAS-konform)
    """

    LOW = "low"
    SUBSTANTIAL = "substantial"
    HIGH = "high"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        substantial: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentificationDataLevelOfAssurance.LOW:
            return low()
        if self is IdentificationDataLevelOfAssurance.SUBSTANTIAL:
            return substantial()
        if self is IdentificationDataLevelOfAssurance.HIGH:
            return high()
