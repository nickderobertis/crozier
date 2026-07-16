

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableContactAssignmentPriority(enum.StrEnum):
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
        if self is WritableContactAssignmentPriority.PRIMARY:
            return primary()
        if self is WritableContactAssignmentPriority.SECONDARY:
            return secondary()
        if self is WritableContactAssignmentPriority.TERTIARY:
            return tertiary()
        if self is WritableContactAssignmentPriority.INACTIVE:
            return inactive()
