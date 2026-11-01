

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MemberState(enum.StrEnum):
    """
    The current status of this subscriber: active, unsubscribed, unconfirmed or cleaned
    """

    ACTIVE = "active"
    DELETED = "deleted"

    def visit(self, active: typing.Callable[[], T_Result], deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is MemberState.ACTIVE:
            return active()
        if self is MemberState.DELETED:
            return deleted()
