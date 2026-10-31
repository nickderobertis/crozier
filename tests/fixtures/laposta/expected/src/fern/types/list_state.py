

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListState(enum.StrEnum):
    """
    Status of the list: active or deleted
    """

    ACTIVE = "active"
    DELETED = "deleted"

    def visit(self, active: typing.Callable[[], T_Result], deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListState.ACTIVE:
            return active()
        if self is ListState.DELETED:
            return deleted()
