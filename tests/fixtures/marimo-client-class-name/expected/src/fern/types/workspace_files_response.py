

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class WorkspaceFilesResponse(UniversalBaseModel):
    file_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="fileCount"), pydantic.Field(alias="fileCount")
    ] = None
    files: typing.List["FileInfo"]
    has_more: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasMore"), pydantic.Field(alias="hasMore")
    ] = None
    root: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .file_info import FileInfo

update_forward_refs(WorkspaceFilesResponse, FileInfo=FileInfo)
