

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class JobFinancialSummaryQuoteSummaryQuoteSummary(UniversalBaseModel):
    quoted_hours: typing_extensions.Annotated[
        float, FieldMetadata(alias="quotedHours"), pydantic.Field(alias="quotedHours")
    ]
    quoted_amount: typing_extensions.Annotated[
        float, FieldMetadata(alias="quotedAmount"), pydantic.Field(alias="quotedAmount")
    ]
    labour: float
    materials: float
    quote_status: typing_extensions.Annotated[
        str, FieldMetadata(alias="quoteStatus"), pydantic.Field(alias="quoteStatus")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
