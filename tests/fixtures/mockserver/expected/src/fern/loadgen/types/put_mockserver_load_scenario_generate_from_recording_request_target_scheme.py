

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme(enum.StrEnum):
    HTTP = "http"
    HTTPS = "https"

    def visit(self, http: typing.Callable[[], T_Result], https: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme.HTTP:
            return http()
        if self is PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme.HTTPS:
            return https()
