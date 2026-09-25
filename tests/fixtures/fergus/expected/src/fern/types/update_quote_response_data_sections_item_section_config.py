

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateQuoteResponseDataSectionsItemSectionConfig(UniversalBaseModel):
    show_all_line_items: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showAllLineItems"), pydantic.Field(alias="showAllLineItems")
    ] = None
    show_prices: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showPrices"), pydantic.Field(alias="showPrices")
    ] = None
    show_totals: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showTotals"), pydantic.Field(alias="showTotals")
    ] = None
    show_summary: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showSummary"), pydantic.Field(alias="showSummary")
    ] = None
    show_quantities: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="showQuantities"), pydantic.Field(alias="showQuantities")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
