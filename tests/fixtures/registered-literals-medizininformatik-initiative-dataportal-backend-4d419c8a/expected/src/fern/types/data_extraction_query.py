

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .data_extraction_query_attribute_groups_item import DataExtractionQueryAttributeGroupsItem


class DataExtractionQuery(UniversalBaseModel):
    attribute_groups: typing_extensions.Annotated[
        typing.List[DataExtractionQueryAttributeGroupsItem],
        FieldMetadata(alias="attributeGroups"),
        pydantic.Field(alias="attributeGroups"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
