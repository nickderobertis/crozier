

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConfidenceScope(enum.StrEnum):
    DETECTION = "detection"
    RECOGNITION = "recognition"
    CLASSIFICATION = "classification"
    GEOMETRY = "geometry"
    ANSWER = "answer"
    QUALITY = "quality"

    def visit(
        self,
        detection: typing.Callable[[], T_Result],
        recognition: typing.Callable[[], T_Result],
        classification: typing.Callable[[], T_Result],
        geometry: typing.Callable[[], T_Result],
        answer: typing.Callable[[], T_Result],
        quality: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConfidenceScope.DETECTION:
            return detection()
        if self is ConfidenceScope.RECOGNITION:
            return recognition()
        if self is ConfidenceScope.CLASSIFICATION:
            return classification()
        if self is ConfidenceScope.GEOMETRY:
            return geometry()
        if self is ConfidenceScope.ANSWER:
            return answer()
        if self is ConfidenceScope.QUALITY:
            return quality()
