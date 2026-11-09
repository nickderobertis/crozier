

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mappable_field_type import MappableFieldType


class GetFieldMappingConfigResponse(UniversalBaseModel):
    can_add_custom_mapping: typing_extensions.Annotated[
        bool, FieldMetadata(alias="canAddCustomMapping"), pydantic.Field(alias="canAddCustomMapping")
    ]
    mappable_fields: typing_extensions.Annotated[
        typing.List[MappableFieldType], FieldMetadata(alias="mappableFields"), pydantic.Field(alias="mappableFields")
    ]
    field_list: typing_extensions.Annotated[
        typing.Any, FieldMetadata(alias="fieldList"), pydantic.Field(alias="fieldList")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
