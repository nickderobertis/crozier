

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .e_tag import ETag
from .file_meta_data_get_file_size import FileMetaDataGetFileSize
from .location_id import LocationId
from .storage_file_id import StorageFileId


class FileMetaDataGet(UniversalBaseModel):
    file_uuid: str = pydantic.Field()
    """
    NOT a unique ID, like (api|uuid)/uuid/file_name or DATCORE folder structure
    """

    location_id: LocationId = pydantic.Field()
    """
    Storage location
    """

    project_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional project name, used by frontend to display path
    """

    node_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional node name, used by frontend to display path
    """

    file_name: str = pydantic.Field()
    """
    Display name for a file
    """

    file_id: StorageFileId = pydantic.Field()
    """
    THIS IS the unique ID for the file. either (api|project_id)/node_id/file_name.ext for S3 and N:package:UUID for datcore
    """

    created_at: dt.datetime
    last_modified: dt.datetime
    file_size: typing.Optional[FileMetaDataGetFileSize] = pydantic.Field(default=None)
    """
    File size in bytes (-1 means invalid)
    """

    entity_tag: typing.Optional[ETag] = pydantic.Field(default=None)
    """
    Entity tag (or ETag), represents a specific version of the file, None if invalid upload or datcore
    """

    is_soft_link: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, this file is a soft link.i.e. is another entry with the same object_name
    """

    is_directory: typing.Optional[bool] = pydantic.Field(default=None)
    """
    if True this is a directory
    """

    sha256checksum: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sha256_checksum"),
        pydantic.Field(
            alias="sha256_checksum",
            description="SHA256 message digest of the file content. Main purpose: cheap lookup.",
        ),
    ] = None
    """
    SHA256 message digest of the file content. Main purpose: cheap lookup.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
