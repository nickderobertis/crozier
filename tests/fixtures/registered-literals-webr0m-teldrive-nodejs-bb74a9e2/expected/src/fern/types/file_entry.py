

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_hash import FileHash
from .file_kind import FileKind
from .file_status import FileStatus
from .uuid_ import Uuid


class FileEntry(UniversalBaseModel):
    id: Uuid
    parent_id: typing_extensions.Annotated[
        typing.Optional[Uuid], FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId")
    ] = None
    name: str
    kind: FileKind
    mime_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType")
    ] = None
    size: typing.Optional[int] = None
    hash: typing.Optional[FileHash] = None
    encryption: bool
    status: FileStatus
    mod_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="modTime"), pydantic.Field(alias="modTime")]
    generation: int
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    parent_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parentPath"),
        pydantic.Field(alias="parentPath", description="Location path, included for drive and recursive listings."),
    ] = None
    """
    Location path, included for drive and recursive listings.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
