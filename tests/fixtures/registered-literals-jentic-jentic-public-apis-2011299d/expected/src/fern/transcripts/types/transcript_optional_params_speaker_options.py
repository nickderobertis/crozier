

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TranscriptOptionalParamsSpeakerOptions(UniversalBaseModel):
    """
    Specify options for [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization#set-a-range-of-possible-speakers). Use this to set a range of possible speakers.
    """

    min_speakers_expected: typing.Optional[int] = pydantic.Field(default=None)
    """
    The minimum number of speakers expected in the audio file. See [Set a range of possible speakers](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization#set-a-range-of-possible-speakers) for more details.
    """

    max_speakers_expected: typing.Optional[int] = pydantic.Field(default=None)
    """
    <Warning>Setting this parameter too high may hurt model accuracy</Warning>
    The maximum number of speakers expected in the audio file. The default depends on audio duration: no limit for 0-2 minutes, 10 for 2-10 minutes, and 30 for 10+ minutes. See [Set a range of possible speakers](https://www.assemblyai.com/docs/pre-recorded-audio/speaker-diarization#set-a-range-of-possible-speakers) for more details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
