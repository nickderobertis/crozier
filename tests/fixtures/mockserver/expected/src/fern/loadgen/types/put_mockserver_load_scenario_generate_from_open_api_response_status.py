

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverLoadScenarioGenerateFromOpenApiResponseStatus(enum.StrEnum):
    LOADED = "loaded"

    def visit(self, loaded: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutMockserverLoadScenarioGenerateFromOpenApiResponseStatus.LOADED:
            return loaded()
