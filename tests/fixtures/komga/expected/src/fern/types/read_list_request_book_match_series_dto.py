

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReadListRequestBookMatchSeriesDto(UniversalBaseModel):
    release_date: typing_extensions.Annotated[
        typing.Optional[dt.date], FieldMetadata(alias="releaseDate"), pydantic.Field(alias="releaseDate")
    ] = None
    series_id: typing_extensions.Annotated[str, FieldMetadata(alias="seriesId"), pydantic.Field(alias="seriesId")]
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
