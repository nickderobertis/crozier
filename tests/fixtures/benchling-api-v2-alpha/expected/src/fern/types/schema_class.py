

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .archive_record import ArchiveRecord


class SchemaClass(UniversalBaseModel):
    archive_record: typing_extensions.Annotated[
        typing.Optional[ArchiveRecord], FieldMetadata(alias="archiveRecord"), pydantic.Field(alias="archiveRecord")
    ] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None
    id: typing.Optional[str] = None
    modified_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="modifiedAt"), pydantic.Field(alias="modifiedAt")
    ] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
