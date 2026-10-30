

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RelatieWijzigenRequestState(enum.StrEnum):
    """
    The new status of the subscriber: active or unsubscribed
    """

    ACTIVE = "active"
    DELETED = "deleted"

    def visit(self, active: typing.Callable[[], T_Result], deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is RelatieWijzigenRequestState.ACTIVE:
            return active()
        if self is RelatieWijzigenRequestState.DELETED:
            return deleted()
