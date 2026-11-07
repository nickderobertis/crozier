

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TranscriptOptionalParamsLanguageDetectionOptions(UniversalBaseModel):
    """
    Specify options for [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection).
    """

    expected_languages: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of languages expected in the audio file. Defaults to `["all"]` when unspecified. See [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) for more details.
    """

    fallback_language: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the detected language of the audio file is not in the list of expected languages, the `fallback_language` is used. Specify `["auto"]` to let our model choose the fallback language from `expected_languages` with the highest confidence score. See [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) for more details.
    """

    code_switching: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether [code switching](/docs/speech-to-text/pre-recorded-audio/code-switching) should be detected.
    """

    code_switching_confidence_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    The confidence threshold for [code switching](/docs/speech-to-text/pre-recorded-audio/code-switching) detection. If the code switching confidence is below this threshold, the transcript will be processed in the language with the highest `language_detection_confidence` score.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
