

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransactionFullVatRatesItem(UniversalBaseModel):
    rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    VAT rate.
    """

    net: typing.Optional[float] = pydantic.Field(default=None)
    """
    NET amount of products having this VAT rate applied.
    """

    vat: typing.Optional[float] = pydantic.Field(default=None)
    """
    VAT amount of this rate applied.
    """

    gross: typing.Optional[float] = pydantic.Field(default=None)
    """
    Gross amount of products having this VAT rate applied.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
