

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .added_at import AddedAt
from .folder_id import FolderId
from .inode import Inode
from .library_id import LibraryId
from .library_item_id import LibraryItemId
from .media_type import MediaType
from .old_library_item_id import OldLibraryItemId
from .updated_at import UpdatedAt


class LibraryItemBase(UniversalBaseModel):
    """
    Base library item schema
    """

    id: typing.Optional[LibraryItemId] = None
    old_library_item_id: typing_extensions.Annotated[
        typing.Optional[OldLibraryItemId],
        FieldMetadata(alias="oldLibraryItemId"),
        pydantic.Field(alias="oldLibraryItemId"),
    ] = None
    ino: typing.Optional[Inode] = None
    library_id: typing_extensions.Annotated[
        typing.Optional[LibraryId], FieldMetadata(alias="libraryId"), pydantic.Field(alias="libraryId")
    ] = None
    folder_id: typing_extensions.Annotated[
        typing.Optional[FolderId], FieldMetadata(alias="folderId"), pydantic.Field(alias="folderId")
    ] = None
    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    The path of the library item on the server.
    """

    rel_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="relPath"),
        pydantic.Field(alias="relPath", description="The path, relative to the library folder, of the library item."),
    ] = None
    """
    The path, relative to the library folder, of the library item.
    """

    is_file: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isFile"),
        pydantic.Field(
            alias="isFile", description="Whether the library item is a single file in the root of the library folder."
        ),
    ] = None
    """
    Whether the library item is a single file in the root of the library folder.
    """

    mtime_ms: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="mtimeMs"),
        pydantic.Field(
            alias="mtimeMs",
            description="The time (in ms since POSIX epoch) when the library item was last modified on disk.",
        ),
    ] = None
    """
    The time (in ms since POSIX epoch) when the library item was last modified on disk.
    """

    ctime_ms: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ctimeMs"),
        pydantic.Field(
            alias="ctimeMs",
            description="The time (in ms since POSIX epoch) when the library item status was changed on disk.",
        ),
    ] = None
    """
    The time (in ms since POSIX epoch) when the library item status was changed on disk.
    """

    birthtime_ms: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="birthtimeMs"),
        pydantic.Field(
            alias="birthtimeMs",
            description="The time (in ms since POSIX epoch) when the library item was created on disk. Will be 0 if unknown.",
        ),
    ] = None
    """
    The time (in ms since POSIX epoch) when the library item was created on disk. Will be 0 if unknown.
    """

    added_at: typing_extensions.Annotated[
        typing.Optional[AddedAt], FieldMetadata(alias="addedAt"), pydantic.Field(alias="addedAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[UpdatedAt], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    is_missing: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isMissing"),
        pydantic.Field(alias="isMissing", description="Whether the library item was scanned and no longer exists."),
    ] = None
    """
    Whether the library item was scanned and no longer exists.
    """

    is_invalid: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isInvalid"),
        pydantic.Field(
            alias="isInvalid", description="Whether the library item was scanned and no longer has media files."
        ),
    ] = None
    """
    Whether the library item was scanned and no longer has media files.
    """

    media_type: typing_extensions.Annotated[
        typing.Optional[MediaType], FieldMetadata(alias="mediaType"), pydantic.Field(alias="mediaType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
