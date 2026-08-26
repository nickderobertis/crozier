

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class FileSearchResponse(UniversalBaseModel):
    files: typing.List["FileInfo"]
    query: str
    total_found: typing_extensions.Annotated[int, FieldMetadata(alias="totalFound"), pydantic.Field(alias="totalFound")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .file_info import FileInfo

update_forward_refs(FileSearchResponse, FileInfo=FileInfo)
