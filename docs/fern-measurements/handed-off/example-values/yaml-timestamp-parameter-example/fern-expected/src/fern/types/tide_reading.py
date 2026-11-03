

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TideReading(UniversalBaseModel):
    level: float
    high_water_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="highWaterAt"), pydantic.Field(alias="highWaterAt")
    ]
    low_water_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lowWaterAt"), pydantic.Field(alias="lowWaterAt")
    ] = None
    calibrated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="calibratedAt"), pydantic.Field(alias="calibratedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
