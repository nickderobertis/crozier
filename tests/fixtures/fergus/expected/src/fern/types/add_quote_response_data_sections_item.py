

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .add_quote_response_data_sections_item_line_items_item import AddQuoteResponseDataSectionsItemLineItemsItem
from .add_quote_response_data_sections_item_section_config import AddQuoteResponseDataSectionsItemSectionConfig
from .add_quote_response_data_sections_item_selection_mode import AddQuoteResponseDataSectionsItemSelectionMode


class AddQuoteResponseDataSectionsItem(UniversalBaseModel):
    section_id: typing_extensions.Annotated[float, FieldMetadata(alias="sectionId"), pydantic.Field(alias="sectionId")]
    name: typing.Optional[str] = None
    sort_order: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="sortOrder"), pydantic.Field(alias="sortOrder")
    ] = None
    parent_section_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="parentSectionId"), pydantic.Field(alias="parentSectionId")
    ] = None
    description: typing.Optional[str] = None
    selection_mode: typing_extensions.Annotated[
        AddQuoteResponseDataSectionsItemSelectionMode,
        FieldMetadata(alias="selectionMode"),
        pydantic.Field(alias="selectionMode"),
    ]
    section_config: typing_extensions.Annotated[
        typing.Optional[AddQuoteResponseDataSectionsItemSectionConfig],
        FieldMetadata(alias="sectionConfig"),
        pydantic.Field(alias="sectionConfig"),
    ] = None
    line_items: typing_extensions.Annotated[
        typing.Optional[typing.List[AddQuoteResponseDataSectionsItemLineItemsItem]],
        FieldMetadata(alias="lineItems"),
        pydantic.Field(alias="lineItems"),
    ] = None
    sections: typing.Optional[typing.List["QuoteSection"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .quote_section import QuoteSection

update_forward_refs(AddQuoteResponseDataSectionsItem, QuoteSection=QuoteSection)
