

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_conversations_conversation_id_offer_request_shipping_price_currency import (
    PostConversationsConversationIdOfferRequestShippingPriceCurrency,
)


class PostConversationsConversationIdOfferRequestShippingPrice(UniversalBaseModel):
    """
    Shipping price (sellers only)
    """

    amount: str = pydantic.Field()
    """
    The amount of money being expressed, as a POSIX-compliant decimal number
    """

    currency: PostConversationsConversationIdOfferRequestShippingPriceCurrency = pydantic.Field()
    """
    The currency the money will be expressed in
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
