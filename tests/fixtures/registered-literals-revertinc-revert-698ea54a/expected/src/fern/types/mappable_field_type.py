

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .common_standard_object import CommonStandardObject


class MappableFieldType(UniversalBaseModel):
    field_name: typing_extensions.Annotated[str, FieldMetadata(alias="fieldName"), pydantic.Field(alias="fieldName")]
    object_name: typing_extensions.Annotated[
        CommonStandardObject, FieldMetadata(alias="objectName"), pydantic.Field(alias="objectName")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
