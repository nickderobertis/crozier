

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HistoricalEventDto(UniversalBaseModel):
    book_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="bookId"), pydantic.Field(alias="bookId")
    ] = None
    id: str
    properties: typing.Dict[str, str]
    series_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="seriesId"), pydantic.Field(alias="seriesId")
    ] = None
    timestamp: dt.datetime
    type: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
