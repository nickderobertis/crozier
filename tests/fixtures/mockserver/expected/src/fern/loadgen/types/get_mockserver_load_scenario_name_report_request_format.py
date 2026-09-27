

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetMockserverLoadScenarioNameReportRequestFormat(enum.StrEnum):
    JUNIT = "junit"

    def visit(self, junit: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetMockserverLoadScenarioNameReportRequestFormat.JUNIT:
            return junit()
