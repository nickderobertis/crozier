

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme(enum.StrEnum):
    HTTP = "http"
    HTTPS = "https"

    def visit(self, http: typing.Callable[[], T_Result], https: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme.HTTP:
            return http()
        if self is PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme.HTTPS:
            return https()
