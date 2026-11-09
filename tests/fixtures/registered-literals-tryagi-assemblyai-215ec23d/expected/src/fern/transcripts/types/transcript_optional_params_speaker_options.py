

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TranscriptOptionalParamsSpeakerOptions(UniversalBaseModel):
    """
    Specify options for [Speaker diarization](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers#set-a-range-of-possible-speakers). Use this to set a range of possible speakers. Requires `speaker_labels` to be `true`, and cannot be used together with `speakers_expected`. When both bounds are set, `min_speakers_expected` must be less than or equal to `max_speakers_expected`.
    """

    min_speakers_expected: typing.Optional[int] = pydantic.Field(default=None)
    """
    A hard lower limit on the number of speaker labels — the model won't return fewer speakers than this. See [Set a range of possible speakers](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers#set-a-range-of-possible-speakers) for more details.
    """

    max_speakers_expected: typing.Optional[int] = pydantic.Field(default=None)
    """
    <Warning>Setting this parameter too high may hurt model accuracy</Warning>
    A hard upper limit on the number of speaker labels. If more people speak than this value, the additional speakers are merged into existing labels. Setting it higher than the true number of speakers can cause the model to over-split and return more speakers than are actually present. The default depends on audio duration: no limit for 0-2 minutes, 10 for 2-10 minutes, and 30 for 10+ minutes. See [Set a range of possible speakers](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers#set-a-range-of-possible-speakers) for more details.
    """

    include_speaker_confidence: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, includes a `speaker_confidence` field per word and per utterance in the response. See [Speaker Diarization](https://www.assemblyai.com/docs/pre-recorded-audio/label-speakers#configuration) for more details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
