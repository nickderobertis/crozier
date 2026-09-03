

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerCheckResponseLevelOfAssurance(enum.StrEnum):
    """
    Sicherheitsniveau der Identifikation
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
        if self is CustomerCheckResponseLevelOfAssurance.LOW:
            return low()
        if self is CustomerCheckResponseLevelOfAssurance.SUBSTANTIAL:
            return substantial()
        if self is CustomerCheckResponseLevelOfAssurance.HIGH:
            return high()
