

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReceiptTransactionVatRatesItem(UniversalBaseModel):
    gross: typing.Optional[float] = pydantic.Field(default=None)
    """
    Gross amount to which the VAT rate applies.
    """

    net: typing.Optional[float] = pydantic.Field(default=None)
    """
    Net amount to which the VAT rate applies.
    """

    rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    VAT rate applied to the transaction amount.
    """

    vat: typing.Optional[float] = pydantic.Field(default=None)
    """
    VAT amount included in the gross amount.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
