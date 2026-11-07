

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    OPENID = "openid"
    """
    openid
    """

    OFFLINE_ACCESS = "offline_access"
    """
    offline access
    """

    EXPENSES_CARD = "expenses.card"
    """
    View and manage card expenses data
    """

    EXPENSES_CARD_READONLY = "expenses.card.readonly"
    """
    View card expenses data
    """

    def visit(
        self,
        openid: typing.Callable[[], T_Result],
        offline_access: typing.Callable[[], T_Result],
        expenses_card: typing.Callable[[], T_Result],
        expenses_card_readonly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.OPENID:
            return openid()
        if self is OauthScope.OFFLINE_ACCESS:
            return offline_access()
        if self is OauthScope.EXPENSES_CARD:
            return expenses_card()
        if self is OauthScope.EXPENSES_CARD_READONLY:
            return expenses_card_readonly()
