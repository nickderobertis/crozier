

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .book_metadata_aggregation_dto import BookMetadataAggregationDto
from .series_metadata_dto import SeriesMetadataDto


class SeriesDto(UniversalBaseModel):
    books_count: typing_extensions.Annotated[int, FieldMetadata(alias="booksCount"), pydantic.Field(alias="booksCount")]
    books_in_progress_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="booksInProgressCount"), pydantic.Field(alias="booksInProgressCount")
    ]
    books_metadata: typing_extensions.Annotated[
        BookMetadataAggregationDto, FieldMetadata(alias="booksMetadata"), pydantic.Field(alias="booksMetadata")
    ]
    books_read_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="booksReadCount"), pydantic.Field(alias="booksReadCount")
    ]
    books_unread_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="booksUnreadCount"), pydantic.Field(alias="booksUnreadCount")
    ]
    created: dt.datetime
    deleted: bool
    file_last_modified: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="fileLastModified"), pydantic.Field(alias="fileLastModified")
    ]
    id: str
    last_modified: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ]
    library_id: typing_extensions.Annotated[str, FieldMetadata(alias="libraryId"), pydantic.Field(alias="libraryId")]
    metadata: SeriesMetadataDto
    name: str
    oneshot: bool
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
