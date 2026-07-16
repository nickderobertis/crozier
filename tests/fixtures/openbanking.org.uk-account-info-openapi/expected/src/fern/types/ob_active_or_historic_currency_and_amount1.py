

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .active_or_historic_currency_code1 import ActiveOrHistoricCurrencyCode1
from .ob_active_currency_and_amount_simple_type import ObActiveCurrencyAndAmountSimpleType


class ObActiveOrHistoricCurrencyAndAmount1(UniversalBaseModel):
    """
    Amount of money to be moved between the debtor and creditor, before deduction of charges, expressed in the currency as ordered by the initiating party.
    Usage: This amount has to be transported unchanged through the transaction chain.
    """

    amount: typing_extensions.Annotated[
        ObActiveCurrencyAndAmountSimpleType, FieldMetadata(alias="Amount"), pydantic.Field(alias="Amount")
    ]
    currency: typing_extensions.Annotated[
        ActiveOrHistoricCurrencyCode1, FieldMetadata(alias="Currency"), pydantic.Field(alias="Currency")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
