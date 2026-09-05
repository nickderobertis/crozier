

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .location_id import LocationId
from .storage_file_id import StorageFileId


class SimCoreFileLink(UniversalBaseModel):
    """
    I/O port type to hold a link to a file in simcore S3 storage
    """

    store: LocationId = pydantic.Field()
    """
    The store identifier: 0 for simcore S3, 1 for datcore
    """

    path: StorageFileId = pydantic.Field()
    """
    The path to the file in the storage provider domain
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    The real file name
    """

    e_tag: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="eTag"),
        pydantic.Field(
            alias="eTag",
            description="Entity tag that uniquely represents the file. The method to generate the tag is not specified (black box).",
        ),
    ] = None
    """
    Entity tag that uniquely represents the file. The method to generate the tag is not specified (black box).
    """

    last_modified: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastModified"),
        pydantic.Field(
            alias="lastModified", description="Timestamp of the last modification of the file, set together with e_tag"
        ),
    ] = None
    """
    Timestamp of the last modification of the file, set together with e_tag
    """

    dataset: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
