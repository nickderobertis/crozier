

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_hash import FileHash
from .name_conflict_policy import NameConflictPolicy
from .uuid_ import Uuid


class UploadCreateRequest(UniversalBaseModel):
    parent_id: typing_extensions.Annotated[
        typing.Optional[Uuid], FieldMetadata(alias="parentId"), pydantic.Field(alias="parentId")
    ] = None
    name: str
    size: int = pydantic.Field()
    """
    Expected size in bytes, or -1 when the size is unknown until completion.
    """

    mime_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType")
    ] = None
    mod_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="modTime"), pydantic.Field(alias="modTime")]
    hash: typing.Optional[FileHash] = None
    encryption: typing.Optional[bool] = None
    conflict_policy: typing_extensions.Annotated[
        typing.Optional[NameConflictPolicy],
        FieldMetadata(alias="conflictPolicy"),
        pydantic.Field(alias="conflictPolicy"),
    ] = None
    preferred_part_size: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="preferredPartSize"),
        pydantic.Field(
            alias="preferredPartSize",
            description="Optional preferred part size. The server may choose a different value.",
        ),
    ] = None
    """
    Optional preferred part size. The server may choose a different value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
