

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TranscriptOptionalParamsDomain(enum.StrEnum):
    """
    Enable domain-specific transcription models to improve accuracy for specialized terminology. Set to `"medical-v1"` to enable [Medical Mode](https://www.assemblyai.com/docs/pre-recorded-audio/medical-mode) for improved accuracy of medical terms such as medications, procedures, conditions, and dosages.

    Supported languages: English (`en`), Spanish (`es`), German (`de`), French (`fr`). If `medical-v1` is used with an unsupported language, the parameter is ignored and a warning is returned.
    """

    MEDICAL_V1 = "medical-v1"

    def visit(self, medical_v1: typing.Callable[[], T_Result]) -> T_Result:
        if self is TranscriptOptionalParamsDomain.MEDICAL_V1:
            return medical_v1()
