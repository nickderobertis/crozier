

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .wp_belongs_to_dto import WpBelongsToDto
from .wp_metadata_dto_reading_progression import WpMetadataDtoReadingProgression


class WpMetadataDto(UniversalBaseModel):
    artist: typing.List[str]
    author: typing.List[str]
    belongs_to: typing_extensions.Annotated[
        typing.Optional[WpBelongsToDto], FieldMetadata(alias="belongsTo"), pydantic.Field(alias="belongsTo")
    ] = None
    colorist: typing.List[str]
    conforms_to: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="conformsTo"), pydantic.Field(alias="conformsTo")
    ] = None
    contributor: typing.List[str]
    description: typing.Optional[str] = None
    editor: typing.List[str]
    identifier: typing.Optional[str] = None
    illustrator: typing.List[str]
    inker: typing.List[str]
    language: typing.Optional[str] = None
    letterer: typing.List[str]
    modified: typing.Optional[dt.datetime] = None
    number_of_pages: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numberOfPages"), pydantic.Field(alias="numberOfPages")
    ] = None
    penciler: typing.List[str]
    published: typing.Optional[dt.date] = None
    publisher: typing.List[str]
    reading_progression: typing_extensions.Annotated[
        typing.Optional[WpMetadataDtoReadingProgression],
        FieldMetadata(alias="readingProgression"),
        pydantic.Field(alias="readingProgression"),
    ] = None
    rendition: typing.Dict[str, typing.Any]
    sort_as: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sortAs"), pydantic.Field(alias="sortAs")
    ] = None
    subject: typing.List[str]
    subtitle: typing.Optional[str] = None
    title: str
    translator: typing.List[str]
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
