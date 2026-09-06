

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .author_dto import AuthorDto


class BookMetadataAggregationDto(UniversalBaseModel):
    authors: typing.List[AuthorDto]
    created: dt.datetime
    last_modified: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ]
    release_date: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="releaseDate"), pydantic.Field(alias="releaseDate")
    ] = None
    summary: str
    summary_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="summaryNumber"), pydantic.Field(alias="summaryNumber")
    ]
    tags: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
