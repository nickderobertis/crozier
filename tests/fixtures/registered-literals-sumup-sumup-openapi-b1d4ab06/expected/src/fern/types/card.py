

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .card_type import CardType


class Card(UniversalBaseModel):
    """
    __Required when payment type is `card`.__ Details of the payment card.
    """

    name: str = pydantic.Field()
    """
    Name of the cardholder as it appears on the payment card.
    """

    number: str = pydantic.Field()
    """
    Number of the payment card (without spaces).
    """

    expiry_year: str = pydantic.Field()
    """
    Two- or four-digit expiration year in `YY` or `YYYY` format.
    """

    expiry_month: str = pydantic.Field()
    """
    Two-digit expiration month, from `01` through `12`.
    """

    cvv: str = pydantic.Field()
    """
    Three or four-digit card verification value (security code) of the payment card.
    """

    zip_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Required five-digit ZIP code. Applicable only to merchant users in the USA.
    """

    type: CardType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
