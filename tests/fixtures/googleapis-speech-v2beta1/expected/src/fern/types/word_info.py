

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WordInfo(UniversalBaseModel):
    """
    Word-specific information for recognized words.
    """

    confidence: typing.Optional[float] = pydantic.Field(default=None)
    """
    Output only. The confidence estimate between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. This field is set only for the top alternative of a non-streaming result or, of a streaming result where `is_final=true`. This field is not guaranteed to be accurate and users should not rely on it to be always provided. The default of 0.0 is a sentinel value indicating `confidence` was not set.
    """

    end_offset: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="endOffset"),
        pydantic.Field(
            alias="endOffset",
            description="Output only. Time offset relative to the beginning of the audio, and corresponding to the end of the spoken word. This field is only set if `enable_word_time_offsets=true` and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary.",
        ),
    ] = None
    """
    Output only. Time offset relative to the beginning of the audio, and corresponding to the end of the spoken word. This field is only set if `enable_word_time_offsets=true` and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary.
    """

    speaker_tag: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="speakerTag"),
        pydantic.Field(
            alias="speakerTag",
            description="Output only. A distinct integer value is assigned for every speaker within the audio. This field specifies which one of those speakers was detected to have spoken this word. Value ranges from `1` to `diarization_config.max_speaker_count` . `speaker_tag` is set if `diarization_config.enable_speaker_diarization` = `true` and only in the top alternative.",
        ),
    ] = None
    """
    Output only. A distinct integer value is assigned for every speaker within the audio. This field specifies which one of those speakers was detected to have spoken this word. Value ranges from `1` to `diarization_config.max_speaker_count` . `speaker_tag` is set if `diarization_config.enable_speaker_diarization` = `true` and only in the top alternative.
    """

    start_offset: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="startOffset"),
        pydantic.Field(
            alias="startOffset",
            description="Output only. Time offset relative to the beginning of the audio, and corresponding to the start of the spoken word. This field is only set if `enable_word_time_offsets=true` and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary.",
        ),
    ] = None
    """
    Output only. Time offset relative to the beginning of the audio, and corresponding to the start of the spoken word. This field is only set if `enable_word_time_offsets=true` and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary.
    """

    word: typing.Optional[str] = pydantic.Field(default=None)
    """
    Output only. The word corresponding to this set of information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
