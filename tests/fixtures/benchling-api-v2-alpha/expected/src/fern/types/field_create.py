

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .field_type import FieldType


class FieldCreate(UniversalBaseModel):
    field_type: typing_extensions.Annotated[
        typing.Optional[FieldType], FieldMetadata(alias="fieldType"), pydantic.Field(alias="fieldType")
    ] = None
    is_multi: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isMulti"), pydantic.Field(alias="isMulti")
    ] = None
    is_parent_link: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isParentLink"), pydantic.Field(alias="isParentLink")
    ] = None
    is_required: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isRequired"), pydantic.Field(alias="isRequired")
    ] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
