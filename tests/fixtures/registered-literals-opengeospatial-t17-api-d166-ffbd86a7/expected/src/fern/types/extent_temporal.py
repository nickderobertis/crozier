

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .extent_temporal_trs import ExtentTemporalTrs


class ExtentTemporal(UniversalBaseModel):
    """
    The temporal extent of the features in the collection.
    """

    interval: typing.Optional[typing.List[typing.List[typing.Optional[dt.datetime]]]] = pydantic.Field(default=None)
    """
    One or more time intervals that describe the temporal extent of the dataset.
    The value `null` is supported and indicates an open time interval.
    In the Core only a single time interval is supported. Extensions may support
    multiple intervals. If multiple intervals are provided, the union of the
    intervals describes the temporal extent.
    """

    trs: typing.Optional[ExtentTemporalTrs] = pydantic.Field(default=None)
    """
    Coordinate reference system of the coordinates in the temporal extent
    (property `interval`). The default reference system is the Gregorian calendar.
    In the Core this is the only supported temporal coordinate reference system.
    Extensions may support additional temporal coordinate reference systems and add
    additional enum values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
