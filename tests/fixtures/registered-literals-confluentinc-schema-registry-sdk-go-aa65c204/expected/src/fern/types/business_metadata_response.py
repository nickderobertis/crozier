

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .error_message import ErrorMessage


class BusinessMetadataResponse(UniversalBaseModel):
    type_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="typeName"), pydantic.Field(alias="typeName")
    ] = None
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None
    entity_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="entityType"), pydantic.Field(alias="entityType")
    ] = None
    entity_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="entityName"), pydantic.Field(alias="entityName")
    ] = None
    error: typing.Optional[ErrorMessage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
