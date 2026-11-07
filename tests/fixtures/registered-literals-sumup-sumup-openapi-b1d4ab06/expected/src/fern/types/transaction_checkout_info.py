

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entry_mode import EntryMode


class TransactionCheckoutInfo(UniversalBaseModel):
    """
    Checkout-specific fields associated with a transaction.
    """

    merchant_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique code of the registered merchant to whom the payment is made.
    """

    vat_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of the applicable VAT (out of the total transaction amount).
    """

    tip_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of the tip (out of the total transaction amount).
    """

    entry_mode: typing.Optional[EntryMode] = None
    auth_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Authorization code for the transaction sent by the payment card issuer or bank. Applicable only to card payments.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
