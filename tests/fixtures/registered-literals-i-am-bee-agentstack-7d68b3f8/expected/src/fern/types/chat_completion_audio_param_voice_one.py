

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatCompletionAudioParamVoiceOne(enum.StrEnum):
    ALLOY = "alloy"
    ASH = "ash"
    BALLAD = "ballad"
    CORAL = "coral"
    ECHO = "echo"
    SAGE = "sage"
    SHIMMER = "shimmer"
    VERSE = "verse"
    MARIN = "marin"
    CEDAR = "cedar"

    def visit(
        self,
        alloy: typing.Callable[[], T_Result],
        ash: typing.Callable[[], T_Result],
        ballad: typing.Callable[[], T_Result],
        coral: typing.Callable[[], T_Result],
        echo: typing.Callable[[], T_Result],
        sage: typing.Callable[[], T_Result],
        shimmer: typing.Callable[[], T_Result],
        verse: typing.Callable[[], T_Result],
        marin: typing.Callable[[], T_Result],
        cedar: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatCompletionAudioParamVoiceOne.ALLOY:
            return alloy()
        if self is ChatCompletionAudioParamVoiceOne.ASH:
            return ash()
        if self is ChatCompletionAudioParamVoiceOne.BALLAD:
            return ballad()
        if self is ChatCompletionAudioParamVoiceOne.CORAL:
            return coral()
        if self is ChatCompletionAudioParamVoiceOne.ECHO:
            return echo()
        if self is ChatCompletionAudioParamVoiceOne.SAGE:
            return sage()
        if self is ChatCompletionAudioParamVoiceOne.SHIMMER:
            return shimmer()
        if self is ChatCompletionAudioParamVoiceOne.VERSE:
            return verse()
        if self is ChatCompletionAudioParamVoiceOne.MARIN:
            return marin()
        if self is ChatCompletionAudioParamVoiceOne.CEDAR:
            return cedar()
