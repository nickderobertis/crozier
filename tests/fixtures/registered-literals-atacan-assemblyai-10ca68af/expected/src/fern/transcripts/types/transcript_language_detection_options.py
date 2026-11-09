

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TranscriptLanguageDetectionOptions(UniversalBaseModel):
    """
    Specify options for Automatic Language Detection.
    """

    expected_languages: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    List of languages expected in the audio file. Defaults to `["all"]` when unspecified.
    """

    fallback_language: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the detected language of the audio file is not in the list of expected languages, the `fallback_language` is used. Specify `["auto"]` to let our model choose the fallback language from `expected_languages` with the highest confidence score.
    """

    code_switching: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether code switching should be detected.
    """

    code_switching_confidence_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    The confidence threshold for code switching detection. If the code switching confidence is below this threshold, the transcript will be processed in the language with the highest `language_detection_confidence` score.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
