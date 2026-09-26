

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QuoteConfig(UniversalBaseModel):
    show_document_totals: typing_extensions.Annotated[
        bool, FieldMetadata(alias="showDocumentTotals"), pydantic.Field(alias="showDocumentTotals")
    ]
    show_line_item_prices: typing_extensions.Annotated[
        bool, FieldMetadata(alias="showLineItemPrices"), pydantic.Field(alias="showLineItemPrices")
    ]
    show_line_item_totals: typing_extensions.Annotated[
        bool, FieldMetadata(alias="showLineItemTotals"), pydantic.Field(alias="showLineItemTotals")
    ]
    show_line_item_quantities: typing_extensions.Annotated[
        bool, FieldMetadata(alias="showLineItemQuantities"), pydantic.Field(alias="showLineItemQuantities")
    ]
    show_section_totals: typing_extensions.Annotated[
        bool, FieldMetadata(alias="showSectionTotals"), pydantic.Field(alias="showSectionTotals")
    ]
    show_labour_prices: typing_extensions.Annotated[
        bool, FieldMetadata(alias="showLabourPrices"), pydantic.Field(alias="showLabourPrices")
    ]
    show_material_prices: typing_extensions.Annotated[
        bool, FieldMetadata(alias="showMaterialPrices"), pydantic.Field(alias="showMaterialPrices")
    ]
    show_labour_summary: typing_extensions.Annotated[
        bool, FieldMetadata(alias="showLabourSummary"), pydantic.Field(alias="showLabourSummary")
    ]
    show_material_summary: typing_extensions.Annotated[
        bool, FieldMetadata(alias="showMaterialSummary"), pydantic.Field(alias="showMaterialSummary")
    ]
    show_all_line_items: typing_extensions.Annotated[
        bool, FieldMetadata(alias="showAllLineItems"), pydantic.Field(alias="showAllLineItems")
    ]
    main_colour: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mainColour"), pydantic.Field(alias="mainColour")
    ] = None
    accent_colour: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="accentColour"), pydantic.Field(alias="accentColour")
    ] = None
    font_colour: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fontColour"), pydantic.Field(alias="fontColour")
    ] = None
    orientation: typing.Optional[str] = None
    font_size_override: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fontSizeOverride"), pydantic.Field(alias="fontSizeOverride")
    ] = None
    indent_customer_address: typing_extensions.Annotated[
        bool, FieldMetadata(alias="indentCustomerAddress"), pydantic.Field(alias="indentCustomerAddress")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
