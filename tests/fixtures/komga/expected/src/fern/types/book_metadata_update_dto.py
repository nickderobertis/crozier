

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .author_update_dto import AuthorUpdateDto
from .web_link_update_dto import WebLinkUpdateDto


class BookMetadataUpdateDto(UniversalBaseModel):
    """
    Metadata fields to update. Set a field to null to unset the metadata. You can omit fields you don't want to update.
    """

    authors: typing.Optional[typing.List[AuthorUpdateDto]] = None
    authors_lock: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="authorsLock"), pydantic.Field(alias="authorsLock")
    ] = None
    isbn: typing.Optional[str] = None
    isbn_lock: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isbnLock"), pydantic.Field(alias="isbnLock")
    ] = None
    links: typing.Optional[typing.List[WebLinkUpdateDto]] = None
    links_lock: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="linksLock"), pydantic.Field(alias="linksLock")
    ] = None
    number: typing.Optional[str] = None
    number_lock: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="numberLock"), pydantic.Field(alias="numberLock")
    ] = None
    number_sort: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="numberSort"), pydantic.Field(alias="numberSort")
    ] = None
    number_sort_lock: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="numberSortLock"), pydantic.Field(alias="numberSortLock")
    ] = None
    release_date: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="releaseDate"), pydantic.Field(alias="releaseDate")
    ] = None
    release_date_lock: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="releaseDateLock"), pydantic.Field(alias="releaseDateLock")
    ] = None
    summary: typing.Optional[str] = None
    summary_lock: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="summaryLock"), pydantic.Field(alias="summaryLock")
    ] = None
    tags: typing.Optional[typing.List[str]] = None
    tags_lock: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="tagsLock"), pydantic.Field(alias="tagsLock")
    ] = None
    title: typing.Optional[str] = None
    title_lock: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="titleLock"), pydantic.Field(alias="titleLock")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
