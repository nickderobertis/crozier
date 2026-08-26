

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class FileDetailsResponse(UniversalBaseModel):
    contents: typing.Optional[str] = None
    file: "FileInfo"
    is_base64: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isBase64"), pydantic.Field(alias="isBase64")
    ] = None
    is_too_large: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isTooLarge"), pydantic.Field(alias="isTooLarge")
    ] = None
    mime_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .file_info import FileInfo

update_forward_refs(FileDetailsResponse, FileInfo=FileInfo)
