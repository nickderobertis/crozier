

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .enhancements import Enhancements


class ClientProvidedEnhancedTransaction(UniversalBaseModel):
    """
    A client-provided transaction that Plaid has enhanced.
    """

    amount: float = pydantic.Field()
    """
    The value of the transaction, denominated in the account's currency, as stated in `iso_currency_code`. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative.
    """

    description: str = pydantic.Field()
    """
    The raw description of the transaction.
    """

    enhancements: Enhancements
    id: str = pydantic.Field()
    """
    Unique transaction identifier to tie transactions back to clients' systems.
    """

    iso_currency_code: str = pydantic.Field()
    """
    The ISO-4217 currency code of the transaction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
