

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AudioIntelligenceModelStatus(enum.StrEnum):
    """
    Either success, or unavailable in the rare case that the model failed
    """

    SUCCESS = "success"
    UNAVAILABLE = "unavailable"

    def visit(self, success: typing.Callable[[], T_Result], unavailable: typing.Callable[[], T_Result]) -> T_Result:
        if self is AudioIntelligenceModelStatus.SUCCESS:
            return success()
        if self is AudioIntelligenceModelStatus.UNAVAILABLE:
            return unavailable()
