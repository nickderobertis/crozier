

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class AdditionalRecipient(UniversalBaseModel):
    """
    Represents an additional recipient (other than the merchant) receiving a portion of this tender.
    """

    amount_money: Money
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the additional recipient.
    """

    location_id: str = pydantic.Field()
    """
    The location ID for a recipient (other than the merchant) receiving a portion of this tender.
    """

    receivable_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID for this [AdditionalRecipientReceivable](https://developer.squareup.com/reference/square_2021-08-18/objects/AdditionalRecipientReceivable), assigned by the server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
