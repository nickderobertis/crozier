

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RedactPiiAudioQuality(enum.StrEnum):
    """
    Controls the filetype of the audio created by redact_pii_audio. Currently supports mp3 (default) and wav. See [PII redaction](https://www.assemblyai.com/docs/models/pii-redaction) for more details.
    """

    MP3 = "mp3"
    """
    MP3 audio format is lower quality and lower size than WAV.
    """

    WAV = "wav"
    """
    WAV audio format is the highest quality (no compression) and larger size than MP3.
    """

    def visit(self, mp3: typing.Callable[[], T_Result], wav: typing.Callable[[], T_Result]) -> T_Result:
        if self is RedactPiiAudioQuality.MP3:
            return mp3()
        if self is RedactPiiAudioQuality.WAV:
            return wav()
