

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListInviteLinksRequestStatus(enum.StrEnum):
    ACTIVE = "active"
    EXPIRED = "expired"
    REVOKED = "revoked"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        revoked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListInviteLinksRequestStatus.ACTIVE:
            return active()
        if self is ListInviteLinksRequestStatus.EXPIRED:
            return expired()
        if self is ListInviteLinksRequestStatus.REVOKED:
            return revoked()
