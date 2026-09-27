

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverLoadScenarioGenerateFromRecordingResponseStatus(enum.StrEnum):
    LOADED = "loaded"

    def visit(self, loaded: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutMockserverLoadScenarioGenerateFromRecordingResponseStatus.LOADED:
            return loaded()
