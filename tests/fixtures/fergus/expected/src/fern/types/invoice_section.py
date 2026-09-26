

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .invoice_section_line_items_item import InvoiceSectionLineItemsItem


class InvoiceSection(UniversalBaseModel):
    section_id: typing_extensions.Annotated[float, FieldMetadata(alias="sectionId"), pydantic.Field(alias="sectionId")]
    name: typing.Optional[str] = None
    sort_order: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="sortOrder"), pydantic.Field(alias="sortOrder")
    ] = None
    parent_section_id: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="parentSectionId"), pydantic.Field(alias="parentSectionId")
    ] = None
    description: typing.Optional[str] = None
    line_items: typing_extensions.Annotated[
        typing.Optional[typing.List[InvoiceSectionLineItemsItem]],
        FieldMetadata(alias="lineItems"),
        pydantic.Field(alias="lineItems"),
    ] = None
    sections: typing.Optional[typing.List["InvoiceSection"]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(InvoiceSection)
