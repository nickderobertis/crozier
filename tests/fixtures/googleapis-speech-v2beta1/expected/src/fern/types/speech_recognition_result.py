

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .speech_recognition_alternative import SpeechRecognitionAlternative


class SpeechRecognitionResult(UniversalBaseModel):
    """
    A speech recognition result corresponding to a portion of the audio.
    """

    alternatives: typing.Optional[typing.List[SpeechRecognitionAlternative]] = pydantic.Field(default=None)
    """
    Output only. May contain one or more recognition hypotheses (up to the maximum specified in `max_alternatives`). These alternatives are ordered in terms of accuracy, with the top (first) alternative being the most probable, as ranked by the recognizer.
    """

    channel_tag: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="channelTag"),
        pydantic.Field(
            alias="channelTag",
            description="Output only. For multi-channel audio, this is the channel number corresponding to the recognized result for the audio from that channel. For `audio_channel_count` = N, its output values can range from `1` to `N`.",
        ),
    ] = None
    """
    Output only. For multi-channel audio, this is the channel number corresponding to the recognized result for the audio from that channel. For `audio_channel_count` = N, its output values can range from `1` to `N`.
    """

    language_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="languageCode"),
        pydantic.Field(
            alias="languageCode",
            description="Output only. The [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag of the language in this result. This language code was detected to have the most likelihood of being spoken in the audio.",
        ),
    ] = None
    """
    Output only. The [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag of the language in this result. This language code was detected to have the most likelihood of being spoken in the audio.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
