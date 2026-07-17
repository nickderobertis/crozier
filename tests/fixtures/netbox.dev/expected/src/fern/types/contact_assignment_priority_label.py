

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContactAssignmentPriorityLabel(enum.StrEnum):
    PRIMARY = "Primary"
    SECONDARY = "Secondary"
    TERTIARY = "Tertiary"
    INACTIVE = "Inactive"

    def visit(
        self,
        primary: typing.Callable[[], T_Result],
        secondary: typing.Callable[[], T_Result],
        tertiary: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactAssignmentPriorityLabel.PRIMARY:
            return primary()
        if self is ContactAssignmentPriorityLabel.SECONDARY:
            return secondary()
        if self is ContactAssignmentPriorityLabel.TERTIARY:
            return tertiary()
        if self is ContactAssignmentPriorityLabel.INACTIVE:
            return inactive()
