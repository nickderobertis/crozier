

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .size import Size


class FileMetadata(UniversalBaseModel):
    """
    The metadata for a file, including the path, size, and unix timestamps of the file.
    """

    filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    The filename of the file.
    """

    ext: typing.Optional[str] = pydantic.Field(default=None)
    """
    The file extension of the file.
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute path on the server of the file.
    """

    rel_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="relPath"),
        pydantic.Field(
            alias="relPath", description="The path of the file, relative to the book's or podcast's folder."
        ),
    ] = None
    """
    The path of the file, relative to the book's or podcast's folder.
    """

    size: typing.Optional[Size] = None
    mtime_ms: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="mtimeMs"),
        pydantic.Field(
            alias="mtimeMs", description="The time (in ms since POSIX epoch) when the file was last modified on disk."
        ),
    ] = None
    """
    The time (in ms since POSIX epoch) when the file was last modified on disk.
    """

    ctime_ms: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ctimeMs"),
        pydantic.Field(
            alias="ctimeMs", description="The time (in ms since POSIX epoch) when the file status was changed on disk."
        ),
    ] = None
    """
    The time (in ms since POSIX epoch) when the file status was changed on disk.
    """

    birthtime_ms: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="birthtimeMs"),
        pydantic.Field(
            alias="birthtimeMs",
            description="The time (in ms since POSIX epoch) when the file was created on disk. Will be 0 if unknown.",
        ),
    ] = None
    """
    The time (in ms since POSIX epoch) when the file was created on disk. Will be 0 if unknown.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
