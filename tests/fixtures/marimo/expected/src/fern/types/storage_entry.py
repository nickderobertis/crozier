

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .storage_entry_kind import StorageEntryKind


class StorageEntry(UniversalBaseModel):
    """
    A storage entry is a file, directory, or object for external storage systems

        Attributes:
            path: The path of the storage entry.
            kind: The kind of the storage entry.
            size: The size of the storage entry.
            last_modified: The last modified time of the storage entry.
            metadata: The metadata of the storage entry.
            mime_type: The MIME type of the storage entry, or None for directories.
    """

    kind: StorageEntryKind
    last_modified: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    mime_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType")
    ] = None
    path: str
    size: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
