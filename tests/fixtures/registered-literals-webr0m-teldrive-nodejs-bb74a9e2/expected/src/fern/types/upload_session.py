

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_hash import FileHash
from .name_conflict_policy import NameConflictPolicy
from .upload_state import UploadState
from .uuid_ import Uuid


class UploadSession(UniversalBaseModel):
    id: Uuid
    parent_id: typing_extensions.Annotated[
        typing.Optional[Uuid], FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId")
    ] = None
    name: str
    expected_size: typing_extensions.Annotated[
        int, FieldMetadata(alias="expectedSize"), pydantic.Field(alias="expectedSize")
    ]
    expected_hash: typing_extensions.Annotated[
        typing.Optional[FileHash], FieldMetadata(alias="expectedHash"), pydantic.Field(alias="expectedHash")
    ] = None
    mime_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType")
    ] = None
    mod_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="modTime"), pydantic.Field(alias="modTime")]
    encryption: bool
    conflict_policy: typing_extensions.Annotated[
        NameConflictPolicy, FieldMetadata(alias="conflictPolicy"), pydantic.Field(alias="conflictPolicy")
    ]
    part_size: typing_extensions.Annotated[int, FieldMetadata(alias="partSize"), pydantic.Field(alias="partSize")]
    state: UploadState
    expires_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ]
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    completed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="completedAt"), pydantic.Field(alias="completedAt")
    ] = None
    file_id: typing_extensions.Annotated[
        typing.Optional[Uuid], FieldMetadata(alias="fileId"), pydantic.Field(alias="fileId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
