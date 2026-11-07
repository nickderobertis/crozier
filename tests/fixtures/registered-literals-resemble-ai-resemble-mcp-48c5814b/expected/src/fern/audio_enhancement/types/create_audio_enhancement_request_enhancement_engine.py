

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateAudioEnhancementRequestEnhancementEngine(enum.StrEnum):
    """
    Enhancement engine to use. Default is v2.
    """

    V1 = "v1"
    V2 = "v2"

    def visit(self, v1: typing.Callable[[], T_Result], v2: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateAudioEnhancementRequestEnhancementEngine.V1:
            return v1()
        if self is CreateAudioEnhancementRequestEnhancementEngine.V2:
            return v2()
