

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GiftCardStatus(enum.StrEnum):
    """
    Indicates the gift card state.
    """

    ACTIVE = "ACTIVE"
    DEACTIVATED = "DEACTIVATED"
    BLOCKED = "BLOCKED"
    PENDING = "PENDING"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        deactivated: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GiftCardStatus.ACTIVE:
            return active()
        if self is GiftCardStatus.DEACTIVATED:
            return deactivated()
        if self is GiftCardStatus.BLOCKED:
            return blocked()
        if self is GiftCardStatus.PENDING:
            return pending()
