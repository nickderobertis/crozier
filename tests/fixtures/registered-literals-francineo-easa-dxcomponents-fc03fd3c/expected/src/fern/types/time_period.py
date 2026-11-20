

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TimePeriod(UniversalBaseModel):
    """
    Defines, if applicable, the limited applicability dates and times of the zone,
    including an eventual daily/weekly schedule
    """

    start_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startDateTime"), pydantic.Field(alias="startDateTime")
    ] = None
    end_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="endDateTime"), pydantic.Field(alias="endDateTime")
    ] = None
    schedule: typing.Optional[typing.List[typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
