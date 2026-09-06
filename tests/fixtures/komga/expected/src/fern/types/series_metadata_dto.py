

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alternate_title_dto import AlternateTitleDto
from .web_link_dto import WebLinkDto


class SeriesMetadataDto(UniversalBaseModel):
    age_rating: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ageRating"), pydantic.Field(alias="ageRating")
    ] = None
    age_rating_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="ageRatingLock"), pydantic.Field(alias="ageRatingLock")
    ]
    alternate_titles: typing_extensions.Annotated[
        typing.List[AlternateTitleDto], FieldMetadata(alias="alternateTitles"), pydantic.Field(alias="alternateTitles")
    ]
    alternate_titles_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="alternateTitlesLock"), pydantic.Field(alias="alternateTitlesLock")
    ]
    created: dt.datetime
    genres: typing.List[str]
    genres_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="genresLock"), pydantic.Field(alias="genresLock")
    ]
    language: str
    language_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="languageLock"), pydantic.Field(alias="languageLock")
    ]
    last_modified: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ]
    links: typing.List[WebLinkDto]
    links_lock: typing_extensions.Annotated[bool, FieldMetadata(alias="linksLock"), pydantic.Field(alias="linksLock")]
    publisher: str
    publisher_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="publisherLock"), pydantic.Field(alias="publisherLock")
    ]
    reading_direction: typing_extensions.Annotated[
        str, FieldMetadata(alias="readingDirection"), pydantic.Field(alias="readingDirection")
    ]
    reading_direction_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="readingDirectionLock"), pydantic.Field(alias="readingDirectionLock")
    ]
    sharing_labels: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="sharingLabels"), pydantic.Field(alias="sharingLabels")
    ]
    sharing_labels_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="sharingLabelsLock"), pydantic.Field(alias="sharingLabelsLock")
    ]
    status: str
    status_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="statusLock"), pydantic.Field(alias="statusLock")
    ]
    summary: str
    summary_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="summaryLock"), pydantic.Field(alias="summaryLock")
    ]
    tags: typing.List[str]
    tags_lock: typing_extensions.Annotated[bool, FieldMetadata(alias="tagsLock"), pydantic.Field(alias="tagsLock")]
    title: str
    title_lock: typing_extensions.Annotated[bool, FieldMetadata(alias="titleLock"), pydantic.Field(alias="titleLock")]
    title_sort: typing_extensions.Annotated[str, FieldMetadata(alias="titleSort"), pydantic.Field(alias="titleSort")]
    title_sort_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="titleSortLock"), pydantic.Field(alias="titleSortLock")
    ]
    total_book_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalBookCount"), pydantic.Field(alias="totalBookCount")
    ] = None
    total_book_count_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="totalBookCountLock"), pydantic.Field(alias="totalBookCountLock")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
