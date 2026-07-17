

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContactAssignmentPriorityValue(enum.StrEnum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    TERTIARY = "tertiary"
    INACTIVE = "inactive"

    def visit(
        self,
        primary: typing.Callable[[], T_Result],
        secondary: typing.Callable[[], T_Result],
        tertiary: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactAssignmentPriorityValue.PRIMARY:
            return primary()
        if self is ContactAssignmentPriorityValue.SECONDARY:
            return secondary()
        if self is ContactAssignmentPriorityValue.TERTIARY:
            return tertiary()
        if self is ContactAssignmentPriorityValue.INACTIVE:
            return inactive()
