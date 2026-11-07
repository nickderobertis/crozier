

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .read_records_response_bearing import ReadRecordsResponseBearing
from .read_records_response_observer import ReadRecordsResponseObserver


class ReadRecordsResponse(UniversalBaseModel):
    observer: typing.Optional[ReadRecordsResponseObserver] = pydantic.Field(default=None)
    """
    Observer of the measurement.
    """

    bearing: typing.Optional[ReadRecordsResponseBearing] = pydantic.Field(default=None)
    """
    The observed bearing.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
