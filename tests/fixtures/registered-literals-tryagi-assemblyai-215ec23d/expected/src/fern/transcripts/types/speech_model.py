

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SpeechModel(enum.StrEnum):
    """
    The speech model to use for the transcription. See [Model Selection](https://www.assemblyai.com/docs/pre-recorded-audio/select-the-speech-model) for available models.
    """

    UNIVERSAL35PRO = "universal-3-5-pro"
    UNIVERSAL2 = "universal-2"

    def visit(
        self, universal35pro: typing.Callable[[], T_Result], universal2: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is SpeechModel.UNIVERSAL35PRO:
            return universal35pro()
        if self is SpeechModel.UNIVERSAL2:
            return universal2()
