

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_currency_currency_code import TaxCloudCurrencyCurrencyCode


class TaxCloudCurrency(UniversalBaseModel):
    currency_code: typing_extensions.Annotated[
        typing.Optional[TaxCloudCurrencyCurrencyCode],
        FieldMetadata(alias="currencyCode"),
        pydantic.Field(
            alias="currencyCode",
            description="ISO 4217 currency code the line-item prices are denominated in. USD or CAD. Defaults to USD when omitted.",
        ),
    ] = None
    """
    ISO 4217 currency code the line-item prices are denominated in. USD or CAD. Defaults to USD when omitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
