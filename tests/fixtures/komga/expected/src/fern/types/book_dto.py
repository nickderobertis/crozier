

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .book_metadata_dto import BookMetadataDto
from .media_dto import MediaDto
from .read_progress_dto import ReadProgressDto


class BookDto(UniversalBaseModel):
    created: dt.datetime
    deleted: bool
    file_hash: typing_extensions.Annotated[str, FieldMetadata(alias="fileHash"), pydantic.Field(alias="fileHash")]
    file_last_modified: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="fileLastModified"), pydantic.Field(alias="fileLastModified")
    ]
    id: str
    last_modified: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ]
    library_id: typing_extensions.Annotated[str, FieldMetadata(alias="libraryId"), pydantic.Field(alias="libraryId")]
    media: MediaDto
    metadata: BookMetadataDto
    name: str
    number: int
    oneshot: bool
    read_progress: typing_extensions.Annotated[
        typing.Optional[ReadProgressDto], FieldMetadata(alias="readProgress"), pydantic.Field(alias="readProgress")
    ] = None
    series_id: typing_extensions.Annotated[str, FieldMetadata(alias="seriesId"), pydantic.Field(alias="seriesId")]
    series_title: typing_extensions.Annotated[
        str, FieldMetadata(alias="seriesTitle"), pydantic.Field(alias="seriesTitle")
    ]
    size: str
    size_bytes: typing_extensions.Annotated[int, FieldMetadata(alias="sizeBytes"), pydantic.Field(alias="sizeBytes")]
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
