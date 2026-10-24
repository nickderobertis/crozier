

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PilotAdsComponentStatus(enum.StrEnum):
    PASSED = "passed"
    BLOCKED = "blocked"

    def visit(self, passed: typing.Callable[[], T_Result], blocked: typing.Callable[[], T_Result]) -> T_Result:
        if self is PilotAdsComponentStatus.PASSED:
            return passed()
        if self is PilotAdsComponentStatus.BLOCKED:
            return blocked()
