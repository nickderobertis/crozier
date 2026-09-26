

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .context_whatsapp_referred_product import ContextWhatsappReferredProduct


class Context(UniversalBaseModel):
    """
    This is only present for the Inbound Message where the user is quoting another message, or for a `product` message where the user has selected the 'Message Business'
    option. It provides information about the quoted message and/or the product message being responded to.
    """

    message_from: str = pydantic.Field()
    """
    The phone number of the **original sender** of the message being quoted in the [E.164](https://en.wikipedia.org/wiki/E.164) format. Not present in a `context` object which is the result of a user selecting 'Message Business' in a `product` message.
    """

    message_uuid: str = pydantic.Field()
    """
    The UUID of the message being quoted. Not present in a `context` object which is the result of a user selecting 'Message Business' in a `product` message.
    """

    whatsapp_referred_product: typing.Optional[ContextWhatsappReferredProduct] = pydantic.Field(default=None)
    """
    An object containing details of a product from a `product` message being quoted or replied to using the 'Message Business' option.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
