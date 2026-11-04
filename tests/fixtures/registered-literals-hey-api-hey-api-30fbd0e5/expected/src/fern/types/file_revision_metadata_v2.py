

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_revision_metadata_v2links import FileRevisionMetadataV2Links
from .file_revision_metadata_v2type import FileRevisionMetadataV2Type


class FileRevisionMetadataV2(UniversalBaseModel):
    """
    A File or Directory's Metadata
    """

    name: str
    id: str = pydantic.Field()
    """
    The id of the resource
    """

    path: str
    version: int
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    type: FileRevisionMetadataV2Type
    links: FileRevisionMetadataV2Links

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
