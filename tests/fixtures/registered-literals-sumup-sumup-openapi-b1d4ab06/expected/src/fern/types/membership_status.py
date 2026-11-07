

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MembershipStatus(enum.StrEnum):
    """
    The status of the membership.
    """

    ACCEPTED = "accepted"
    PENDING = "pending"
    EXPIRED = "expired"
    DISABLED = "disabled"
    UNKNOWN = "unknown"

    def visit(
        self,
        accepted: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MembershipStatus.ACCEPTED:
            return accepted()
        if self is MembershipStatus.PENDING:
            return pending()
        if self is MembershipStatus.EXPIRED:
            return expired()
        if self is MembershipStatus.DISABLED:
            return disabled()
        if self is MembershipStatus.UNKNOWN:
            return unknown()
