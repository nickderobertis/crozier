

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.audio_timestamps import AudioTimestamps


class SynthesizeResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    audio_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base64-encoded audio bytes
    """

    audio_timestamps: typing.Optional[AudioTimestamps] = None
    duration: typing.Optional[float] = pydantic.Field(default=None)
    """
    Audio duration in seconds
    """

    synth_duration: typing.Optional[float] = pydantic.Field(default=None)
    """
    Raw synthesis time
    """

    output_format: typing.Optional[str] = None
    sample_rate: typing.Optional[int] = None
    title: typing.Optional[str] = None
    issues: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
