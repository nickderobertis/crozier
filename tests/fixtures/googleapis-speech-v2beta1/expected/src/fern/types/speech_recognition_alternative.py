

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .word_info import WordInfo


class SpeechRecognitionAlternative(UniversalBaseModel):
    """
    Alternative hypotheses (a.k.a. n-best list).
    """

    confidence: typing.Optional[float] = pydantic.Field(default=None)
    """
    Output only. The confidence estimate between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. This field is set only for the top alternative of a non-streaming result or, of a streaming result where `is_final=true`. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating `confidence` was not set.
    """

    transcript: typing.Optional[str] = pydantic.Field(default=None)
    """
    Output only. Transcript text representing the words that the user spoke.
    """

    words: typing.Optional[typing.List[WordInfo]] = pydantic.Field(default=None)
    """
    Output only. A list of word-specific information for each recognized word. Note: When `enable_speaker_diarization` is true, you will see all the words from the beginning of the audio.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
