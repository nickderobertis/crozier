

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1GetJitAccessConfigResponseAppliedSuccessfullyState(enum.StrEnum):
    ENABLED = "enabled"
    DISABLED = "disabled"

    def visit(self, enabled: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1GetJitAccessConfigResponseAppliedSuccessfullyState.ENABLED:
            return enabled()
        if self is V1GetJitAccessConfigResponseAppliedSuccessfullyState.DISABLED:
            return disabled()
