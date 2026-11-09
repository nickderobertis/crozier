

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TranscriptOptionalParamsSpeakerOptions(UniversalBaseModel):
    """
    Specify options for speaker diarization.
    """

    min_speakers_expected: typing.Optional[int] = pydantic.Field(default=None)
    """
    The minimum number of speakers expected in the audio file.
    """

    max_speakers_expected: typing.Optional[int] = pydantic.Field(default=None)
    """
    <Warning>Setting this parameter too high may hurt model accuracy</Warning>
    The maximum number of speakers expected in the audio file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
