

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .data_extraction_query_attribute_groups_item_attributes_item import (
    DataExtractionQueryAttributeGroupsItemAttributesItem,
)
from .data_extraction_query_attribute_groups_item_filter_item import DataExtractionQueryAttributeGroupsItemFilterItem


class DataExtractionQueryAttributeGroupsItem(UniversalBaseModel):
    id: str
    name: typing.Optional[str] = None
    group_reference: typing_extensions.Annotated[
        str, FieldMetadata(alias="groupReference"), pydantic.Field(alias="groupReference")
    ]
    include_reference_only: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="includeReferenceOnly"), pydantic.Field(alias="includeReferenceOnly")
    ] = None
    attributes: typing.List[DataExtractionQueryAttributeGroupsItemAttributesItem]
    filter: typing.Optional[typing.List[DataExtractionQueryAttributeGroupsItemFilterItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
