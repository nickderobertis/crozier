

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSpeechRequestVoice(enum.StrEnum):
    """
    The voice to use when generating the audio. Supported voices are `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer`. Previews of the voices are available in the [Text to speech guide](/docs/guides/text-to-speech/voice-options).
    """

    ALLOY = "alloy"
    ECHO = "echo"
    FABLE = "fable"
    ONYX = "onyx"
    NOVA = "nova"
    SHIMMER = "shimmer"

    def visit(
        self,
        alloy: typing.Callable[[], T_Result],
        echo: typing.Callable[[], T_Result],
        fable: typing.Callable[[], T_Result],
        onyx: typing.Callable[[], T_Result],
        nova: typing.Callable[[], T_Result],
        shimmer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateSpeechRequestVoice.ALLOY:
            return alloy()
        if self is CreateSpeechRequestVoice.ECHO:
            return echo()
        if self is CreateSpeechRequestVoice.FABLE:
            return fable()
        if self is CreateSpeechRequestVoice.ONYX:
            return onyx()
        if self is CreateSpeechRequestVoice.NOVA:
            return nova()
        if self is CreateSpeechRequestVoice.SHIMMER:
            return shimmer()
