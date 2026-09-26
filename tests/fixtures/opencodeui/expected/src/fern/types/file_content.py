

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_content_encoding import FileContentEncoding
from .file_content_patch import FileContentPatch
from .file_content_type import FileContentType


class FileContent(UniversalBaseModel):
    type: FileContentType
    content: str
    diff: typing.Optional[str] = None
    patch: typing.Optional[FileContentPatch] = None
    encoding: typing.Optional[FileContentEncoding] = None
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
