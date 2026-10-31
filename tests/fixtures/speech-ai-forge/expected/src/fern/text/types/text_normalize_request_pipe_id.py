

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TextNormalizeRequestPipeId(enum.StrEnum):
    BASE = "base"
    CHAT_TTS = "chat-tts"
    COSY_VOICE = "cosy-voice"
    FISH_SPEECH = "fish-speech"
    F5TTS = "f5-tts"
    INDEX_TTS = "index-tts"
    SPARK_TTS = "spark-tts"

    def visit(
        self,
        base: typing.Callable[[], T_Result],
        chat_tts: typing.Callable[[], T_Result],
        cosy_voice: typing.Callable[[], T_Result],
        fish_speech: typing.Callable[[], T_Result],
        f5tts: typing.Callable[[], T_Result],
        index_tts: typing.Callable[[], T_Result],
        spark_tts: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextNormalizeRequestPipeId.BASE:
            return base()
        if self is TextNormalizeRequestPipeId.CHAT_TTS:
            return chat_tts()
        if self is TextNormalizeRequestPipeId.COSY_VOICE:
            return cosy_voice()
        if self is TextNormalizeRequestPipeId.FISH_SPEECH:
            return fish_speech()
        if self is TextNormalizeRequestPipeId.F5TTS:
            return f5tts()
        if self is TextNormalizeRequestPipeId.INDEX_TTS:
            return index_tts()
        if self is TextNormalizeRequestPipeId.SPARK_TTS:
            return spark_tts()
