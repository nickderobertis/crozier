

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FieldMappingType(UniversalBaseModel):
    source_field_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="sourceFieldName"), pydantic.Field(alias="sourceFieldName")
    ]
    target_field_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="targetFieldName"), pydantic.Field(alias="targetFieldName")
    ]
    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
