

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .timestamp import Timestamp
from .timestamp_created import TimestampCreated


class TimestampObjLeg(UniversalBaseModel):
    end: typing.Optional[Timestamp] = None
    request: typing.Optional[Timestamp] = None
    start: typing.Optional[TimestampCreated] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
