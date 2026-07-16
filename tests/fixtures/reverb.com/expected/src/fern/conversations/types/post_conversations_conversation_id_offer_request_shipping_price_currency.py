

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostConversationsConversationIdOfferRequestShippingPriceCurrency(str, enum.Enum):
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
        if self is PostConversationsConversationIdOfferRequestShippingPriceCurrency.USD:
            return usd()
        if self is PostConversationsConversationIdOfferRequestShippingPriceCurrency.CAD:
            return cad()
        if self is PostConversationsConversationIdOfferRequestShippingPriceCurrency.EUR:
            return eur()
        if self is PostConversationsConversationIdOfferRequestShippingPriceCurrency.GBP:
            return gbp()
        if self is PostConversationsConversationIdOfferRequestShippingPriceCurrency.AUD:
            return aud()
        if self is PostConversationsConversationIdOfferRequestShippingPriceCurrency.JPY:
            return jpy()
        if self is PostConversationsConversationIdOfferRequestShippingPriceCurrency.NZD:
            return nzd()
        if self is PostConversationsConversationIdOfferRequestShippingPriceCurrency.MXN:
            return mxn()
