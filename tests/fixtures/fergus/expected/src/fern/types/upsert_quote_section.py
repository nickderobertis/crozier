

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .upsert_quote_section_favourite_section_id import UpsertQuoteSectionFavouriteSectionId
from .upsert_quote_section_favourite_section_ids import UpsertQuoteSectionFavouriteSectionIds
from .upsert_quote_section_line_items_item import UpsertQuoteSectionLineItemsItem


class UpsertQuoteSection(UniversalBaseModel):
    name: str
    favourite_section_id: typing_extensions.Annotated[
        typing.Optional[UpsertQuoteSectionFavouriteSectionId],
        FieldMetadata(alias="favouriteSectionId"),
        pydantic.Field(alias="favouriteSectionId"),
    ] = None
    favourite_section_ids: typing_extensions.Annotated[
        typing.Optional[UpsertQuoteSectionFavouriteSectionIds],
        FieldMetadata(alias="favouriteSectionIds"),
        pydantic.Field(alias="favouriteSectionIds"),
    ] = None
    section_line_item_multiplier: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="sectionLineItemMultiplier"),
        pydantic.Field(alias="sectionLineItemMultiplier"),
    ] = None
    parent_section_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="parentSectionId"), pydantic.Field(alias="parentSectionId")
    ] = None
    description: typing.Optional[str] = None
    sort_order: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="sortOrder"), pydantic.Field(alias="sortOrder")
    ] = None
    line_items: typing_extensions.Annotated[
        typing.Optional[typing.List[UpsertQuoteSectionLineItemsItem]],
        FieldMetadata(alias="lineItems"),
        pydantic.Field(alias="lineItems"),
    ] = None
    sections: typing.Optional[typing.List["UpsertQuoteSection"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(UpsertQuoteSection)
