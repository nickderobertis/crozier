

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostConversationsConversationIdOfferRequestPriceCurrency(enum.StrEnum):
    """
    The currency the money will be expressed in
    """

    USD = "USD"
    CAD = "CAD"
    EUR = "EUR"
    GBP = "GBP"
    AUD = "AUD"
    JPY = "JPY"
    NZD = "NZD"
    MXN = "MXN"

    def visit(
        self,
        usd: typing.Callable[[], T_Result],
        cad: typing.Callable[[], T_Result],
        eur: typing.Callable[[], T_Result],
        gbp: typing.Callable[[], T_Result],
        aud: typing.Callable[[], T_Result],
        jpy: typing.Callable[[], T_Result],
        nzd: typing.Callable[[], T_Result],
        mxn: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostConversationsConversationIdOfferRequestPriceCurrency.USD:
            return usd()
        if self is PostConversationsConversationIdOfferRequestPriceCurrency.CAD:
            return cad()
        if self is PostConversationsConversationIdOfferRequestPriceCurrency.EUR:
            return eur()
        if self is PostConversationsConversationIdOfferRequestPriceCurrency.GBP:
            return gbp()
        if self is PostConversationsConversationIdOfferRequestPriceCurrency.AUD:
            return aud()
        if self is PostConversationsConversationIdOfferRequestPriceCurrency.JPY:
            return jpy()
        if self is PostConversationsConversationIdOfferRequestPriceCurrency.NZD:
            return nzd()
        if self is PostConversationsConversationIdOfferRequestPriceCurrency.MXN:
            return mxn()
