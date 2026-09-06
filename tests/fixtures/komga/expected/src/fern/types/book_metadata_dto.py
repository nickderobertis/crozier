

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .author_dto import AuthorDto
from .web_link_dto import WebLinkDto


class BookMetadataDto(UniversalBaseModel):
    authors: typing.List[AuthorDto]
    authors_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="authorsLock"), pydantic.Field(alias="authorsLock")
    ]
    created: dt.datetime
    isbn: str
    isbn_lock: typing_extensions.Annotated[bool, FieldMetadata(alias="isbnLock"), pydantic.Field(alias="isbnLock")]
    last_modified: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ]
    links: typing.List[WebLinkDto]
    links_lock: typing_extensions.Annotated[bool, FieldMetadata(alias="linksLock"), pydantic.Field(alias="linksLock")]
    number: str
    number_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="numberLock"), pydantic.Field(alias="numberLock")
    ]
    number_sort: typing_extensions.Annotated[
        float, FieldMetadata(alias="numberSort"), pydantic.Field(alias="numberSort")
    ]
    number_sort_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="numberSortLock"), pydantic.Field(alias="numberSortLock")
    ]
    release_date: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="releaseDate"), pydantic.Field(alias="releaseDate")
    ] = None
    release_date_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="releaseDateLock"), pydantic.Field(alias="releaseDateLock")
    ]
    summary: str
    summary_lock: typing_extensions.Annotated[
        bool, FieldMetadata(alias="summaryLock"), pydantic.Field(alias="summaryLock")
    ]
    tags: typing.List[str]
    tags_lock: typing_extensions.Annotated[bool, FieldMetadata(alias="tagsLock"), pydantic.Field(alias="tagsLock")]
    title: str
    title_lock: typing_extensions.Annotated[bool, FieldMetadata(alias="titleLock"), pydantic.Field(alias="titleLock")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
