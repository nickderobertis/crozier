

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .field_schema import FieldSchema


class FieldSchemaUpdate(UniversalBaseModel):
    new_schema: typing_extensions.Annotated[
        FieldSchema, FieldMetadata(alias="newSchema"), pydantic.Field(alias="newSchema")
    ]
    old_schema: typing_extensions.Annotated[
        FieldSchema, FieldMetadata(alias="oldSchema"), pydantic.Field(alias="oldSchema")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
