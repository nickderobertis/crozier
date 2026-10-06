

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recording_format import RecordingFormat
from .recording_limits import RecordingLimits


class RecordingCapabilities(UniversalBaseModel):
    enabled: bool
    format: RecordingFormat
    limits: RecordingLimits

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
