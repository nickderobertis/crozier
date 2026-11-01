

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FieldState(enum.StrEnum):
    """
    The status of the field in question: either active or deleted
    """

    ACTIVE = "active"
    DELETED = "deleted"

    def visit(self, active: typing.Callable[[], T_Result], deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is FieldState.ACTIVE:
            return active()
        if self is FieldState.DELETED:
            return deleted()
