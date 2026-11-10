

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WalletBalance(UniversalBaseModel):
    """
    An object representing the e-wallet balance
    """

    current: float = pydantic.Field()
    """
    The total amount of funds in the account
    """

    iso_currency_code: str = pydantic.Field()
    """
    The ISO-4217 currency code of the balance
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
