

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .active_or_historic_currency_code1 import ActiveOrHistoricCurrencyCode1
from .ob_active_currency_and_amount_simple_type import ObActiveCurrencyAndAmountSimpleType


class ObActiveOrHistoricCurrencyAndAmount7(UniversalBaseModel):
    """
    Amount of money associated with the statement interest amount type.
    """

    amount: typing_extensions.Annotated[ObActiveCurrencyAndAmountSimpleType, FieldMetadata(alias="Amount")]
    currency: typing_extensions.Annotated[ActiveOrHistoricCurrencyCode1, FieldMetadata(alias="Currency")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
