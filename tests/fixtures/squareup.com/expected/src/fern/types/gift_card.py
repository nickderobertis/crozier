

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gan_source import GanSource
from .money import Money
from .status import Status
from .type import Type


class GiftCard(UniversalBaseModel):
    """
    Represents a Square gift card.
    """

    balance_money: typing.Optional[Money] = None
    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the gift card was created, in RFC 3339 format. 
    In the case of a digital gift card, it is the time when you create a card 
    (using the Square Point of Sale application, Seller Dashboard, or Gift Cards API).  
    In the case of a plastic gift card, it is the time when Square associates the card with the 
    seller at the time of activation.
    """

    customer_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The IDs of the customers to whom this gift card is linked.
    """

    gan: typing.Optional[str] = pydantic.Field(default=None)
    """
    The gift card account number.
    """

    gan_source: typing.Optional[GanSource] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-assigned ID of the gift card.
    """

    state: typing.Optional[Status] = None
    type: Type

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
