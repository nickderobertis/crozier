

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubAccountStatus(enum.StrEnum):
    """
    Current sub-account status
    """

    ACTIVE = "active"
    SUSPENDED = "suspended"
    PARENT_SUSPENDED = "parent-suspended"
    DELETED = "deleted"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        suspended: typing.Callable[[], T_Result],
        parent_suspended: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubAccountStatus.ACTIVE:
            return active()
        if self is SubAccountStatus.SUSPENDED:
            return suspended()
        if self is SubAccountStatus.PARENT_SUSPENDED:
            return parent_suspended()
        if self is SubAccountStatus.DELETED:
            return deleted()
