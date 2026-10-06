

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recording_format_codec import RecordingFormatCodec
from .recording_format_container import RecordingFormatContainer


class RecordingFormat(UniversalBaseModel):
    bits_per_sample: int
    bytes_per_second: int
    channels: int
    codec: RecordingFormatCodec
    container: RecordingFormatContainer
    sample_rate: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
