

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TranscriptOptionalParamsLanguageDetectionOptionsOnNoSpeechDetected(enum.StrEnum):
    """
    Controls what happens when no speech is detected in the audio. With `error` (the default), the transcript fails and the reason is returned in `error`. With `fallback`, the transcript completes with an empty `text`, `language_code` is set to the `fallback_language`, and an explanatory warning is returned in `metadata.warnings`.

    `fallback` requires `fallback_language` to be set to a specific language code; `auto` returns a `400`. See [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) for more details.
    """

    ERROR = "error"
    FALLBACK = "fallback"

    def visit(self, error: typing.Callable[[], T_Result], fallback: typing.Callable[[], T_Result]) -> T_Result:
        if self is TranscriptOptionalParamsLanguageDetectionOptionsOnNoSpeechDetected.ERROR:
            return error()
        if self is TranscriptOptionalParamsLanguageDetectionOptionsOnNoSpeechDetected.FALLBACK:
            return fallback()
