

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .any import Any


class CacheItem(UniversalBaseModel):
    """
    a single entry in the results of a status query when `--verbose` is enabled
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    the type of the cache
    """

    items: typing.Optional[typing.List[Any]] = pydantic.Field(default=None)
    """
    the individual items in the cache (if --verbose)
    """

    last_cached: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastCached"),
        pydantic.Field(alias="lastCached", description="the date of the most recent item added to the cache"),
    ] = None
    """
    the date of the most recent item added to the cache
    """

    n_files: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nFiles"),
        pydantic.Field(alias="nFiles", description="the number of items in the cache"),
    ] = None
    """
    the number of items in the cache
    """

    n_folders: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="nFolders"),
        pydantic.Field(alias="nFolders", description="the number of folders holding that many items"),
    ] = None
    """
    the number of folders holding that many items
    """

    path: typing.Optional[str] = pydantic.Field(default=None)
    """
    the path to the top of the given cache
    """

    size_in_bytes: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sizeInBytes"),
        pydantic.Field(alias="sizeInBytes", description="the size of the cache in bytes"),
    ] = None
    """
    the size of the cache in bytes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
