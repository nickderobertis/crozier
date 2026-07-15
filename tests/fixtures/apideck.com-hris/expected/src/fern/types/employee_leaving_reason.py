

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EmployeeLeavingReason(str, enum.Enum):
    """
    The reason because the employment ended.
    """

    DISMISSED = "dismissed"
    RESIGNED = "resigned"
    REDUNDANCY = "redundancy"
    OTHER = "other"

    def visit(
        self,
        dismissed: typing.Callable[[], T_Result],
        resigned: typing.Callable[[], T_Result],
        redundancy: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmployeeLeavingReason.DISMISSED:
            return dismissed()
        if self is EmployeeLeavingReason.RESIGNED:
            return resigned()
        if self is EmployeeLeavingReason.REDUNDANCY:
            return redundancy()
        if self is EmployeeLeavingReason.OTHER:
            return other()
