

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CodeSubscriptionResponseStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    TRIGGERED = "TRIGGERED"
    DELIVERED = "DELIVERED"
    RESOLVED = "RESOLVED"
    OBSOLETE = "OBSOLETE"
    DELETED = "DELETED"
    ERROR = "ERROR"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        triggered: typing.Callable[[], T_Result],
        delivered: typing.Callable[[], T_Result],
        resolved: typing.Callable[[], T_Result],
        obsolete: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CodeSubscriptionResponseStatus.ACTIVE:
            return active()
        if self is CodeSubscriptionResponseStatus.TRIGGERED:
            return triggered()
        if self is CodeSubscriptionResponseStatus.DELIVERED:
            return delivered()
        if self is CodeSubscriptionResponseStatus.RESOLVED:
            return resolved()
        if self is CodeSubscriptionResponseStatus.OBSOLETE:
            return obsolete()
        if self is CodeSubscriptionResponseStatus.DELETED:
            return deleted()
        if self is CodeSubscriptionResponseStatus.ERROR:
            return error()
