

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobAssignmentPayType(enum.StrEnum):
    """
    Enumerates the possible pay types that a job can be assigned.
    """

    NONE = "NONE"
    HOURLY = "HOURLY"
    SALARY = "SALARY"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        hourly: typing.Callable[[], T_Result],
        salary: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JobAssignmentPayType.NONE:
            return none()
        if self is JobAssignmentPayType.HOURLY:
            return hourly()
        if self is JobAssignmentPayType.SALARY:
            return salary()
