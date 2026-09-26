

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Ok16(UniversalBaseModel):
    file_bytes: typing_extensions.Annotated[str, FieldMetadata(alias="FileBytes"), pydantic.Field(alias="FileBytes")]
    file_name: typing_extensions.Annotated[str, FieldMetadata(alias="FileName"), pydantic.Field(alias="FileName")]
    mime_type: typing_extensions.Annotated[str, FieldMetadata(alias="MimeType"), pydantic.Field(alias="MimeType")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
