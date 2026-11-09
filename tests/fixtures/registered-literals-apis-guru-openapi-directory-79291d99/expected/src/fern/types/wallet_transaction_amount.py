

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wallet_iso_currency_code import WalletIsoCurrencyCode


class WalletTransactionAmount(UniversalBaseModel):
    """
    The amount and currency of a transaction
    """

    iso_currency_code: WalletIsoCurrencyCode
    value: float = pydantic.Field()
    """
    The amount of the transaction. Must contain at most two digits of precision e.g. `1.23`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
