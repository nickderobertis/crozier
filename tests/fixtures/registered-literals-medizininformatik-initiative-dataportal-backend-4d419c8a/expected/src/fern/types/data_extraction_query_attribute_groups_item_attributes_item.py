

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DataExtractionQueryAttributeGroupsItemAttributesItem(UniversalBaseModel):
    attribute_ref: typing_extensions.Annotated[
        str, FieldMetadata(alias="attributeRef"), pydantic.Field(alias="attributeRef")
    ]
    must_have: typing_extensions.Annotated[bool, FieldMetadata(alias="mustHave"), pydantic.Field(alias="mustHave")]
    linked_groups: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="linkedGroups"), pydantic.Field(alias="linkedGroups")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
