

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_language_detection_options_on_no_speech_detected import (
    TranscriptLanguageDetectionOptionsOnNoSpeechDetected,
)


class TranscriptLanguageDetectionOptions(UniversalBaseModel):
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
    Whether [code switching](/speech-to-text/pre-recorded-audio/code-switching) should be detected.
    """

    code_switching_confidence_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    The confidence threshold for [code switching](/speech-to-text/pre-recorded-audio/code-switching) detection. If the code switching confidence is below this threshold, the transcript will be processed in the language with the highest `language_detection_confidence` score.
    """

    localization: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Render the transcript in a regional variant of the detected language. Supported values are `en_au` (Australian English) and `en_uk` (British English) — only English is supported today, and you can specify at most one locale per base language. Base or default-region codes such as `en` and `en_us` are not localization variants and return a `400`.
    
    When the detected language matches the requested locale's base language, the transcript uses that locale's spelling and `language_code` returns the region-aware code (for example `en_au`) instead of the base `en`. Otherwise, when the detected language isn't available as a locale, the option is ignored. See [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) for more details.
    """

    on_no_speech_detected: typing.Optional[TranscriptLanguageDetectionOptionsOnNoSpeechDetected] = pydantic.Field(
        default=None
    )
    """
    Controls what happens when no speech is detected in the audio. With `error` (the default), the transcript fails and the reason is returned in `error`. With `fallback`, the transcript completes with an empty `text`, `language_code` is set to the `fallback_language`, and an explanatory warning is returned in `metadata.warnings`.
    
    `fallback` requires `fallback_language` to be set to a specific language code; `auto` returns a `400`. See [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) for more details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
