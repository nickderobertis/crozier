

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class ChargeRequestAdditionalRecipient(UniversalBaseModel):
    """
    Represents an additional recipient (other than the merchant) entitled to a portion of the tender.
    Support is currently limited to USD, CAD and GBP currencies
    """

    amount_money: Money
    description: str = pydantic.Field()
    """
    The description of the additional recipient.
    """

    location_id: str = pydantic.Field()
    """
    The location ID for a recipient (other than the merchant) receiving a portion of the tender.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
