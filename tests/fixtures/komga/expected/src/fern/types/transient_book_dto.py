

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .page_dto import PageDto


class TransientBookDto(UniversalBaseModel):
    comment: str
    file_last_modified: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="fileLastModified"), pydantic.Field(alias="fileLastModified")
    ]
    files: typing.List[str]
    id: str
    media_type: typing_extensions.Annotated[str, FieldMetadata(alias="mediaType"), pydantic.Field(alias="mediaType")]
    name: str
    number: typing.Optional[float] = None
    pages: typing.List[PageDto]
    series_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="seriesId"), pydantic.Field(alias="seriesId")
    ] = None
    size: str
    size_bytes: typing_extensions.Annotated[int, FieldMetadata(alias="sizeBytes"), pydantic.Field(alias="sizeBytes")]
    status: str
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
