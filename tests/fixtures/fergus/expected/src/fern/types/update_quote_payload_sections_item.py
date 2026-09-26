

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .update_quote_payload_sections_item_favourite_section_id import UpdateQuotePayloadSectionsItemFavouriteSectionId
from .update_quote_payload_sections_item_favourite_section_ids import UpdateQuotePayloadSectionsItemFavouriteSectionIds
from .update_quote_payload_sections_item_line_items_item import UpdateQuotePayloadSectionsItemLineItemsItem


class UpdateQuotePayloadSectionsItem(UniversalBaseModel):
    name: str
    favourite_section_id: typing_extensions.Annotated[
        typing.Optional[UpdateQuotePayloadSectionsItemFavouriteSectionId],
        FieldMetadata(alias="favouriteSectionId"),
        pydantic.Field(alias="favouriteSectionId"),
    ] = None
    favourite_section_ids: typing_extensions.Annotated[
        typing.Optional[UpdateQuotePayloadSectionsItemFavouriteSectionIds],
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
        typing.Optional[typing.List[UpdateQuotePayloadSectionsItemLineItemsItem]],
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


from .upsert_quote_section import UpsertQuoteSection

update_forward_refs(UpdateQuotePayloadSectionsItem, UpsertQuoteSection=UpsertQuoteSection)
