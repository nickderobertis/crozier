

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .quote_totals_quote_total import QuoteTotalsQuoteTotal
from .quote_totals_section_totals_item import QuoteTotalsSectionTotalsItem


class QuoteTotals(UniversalBaseModel):
    section_totals: typing_extensions.Annotated[
        typing.List[QuoteTotalsSectionTotalsItem],
        FieldMetadata(alias="sectionTotals"),
        pydantic.Field(alias="sectionTotals"),
    ]
    quote_total: typing_extensions.Annotated[
        QuoteTotalsQuoteTotal, FieldMetadata(alias="quoteTotal"), pydantic.Field(alias="quoteTotal")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
