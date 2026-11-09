

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AnnotationQueueObjectType(enum.StrEnum):
    TRACE = "TRACE"
    OBSERVATION = "OBSERVATION"

    def visit(self, trace: typing.Callable[[], T_Result], observation: typing.Callable[[], T_Result]) -> T_Result:
        if self is AnnotationQueueObjectType.TRACE:
            return trace()
        if self is AnnotationQueueObjectType.OBSERVATION:
            return observation()
