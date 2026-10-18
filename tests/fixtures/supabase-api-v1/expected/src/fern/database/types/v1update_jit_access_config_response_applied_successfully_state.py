

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1UpdateJitAccessConfigResponseAppliedSuccessfullyState(enum.StrEnum):
    ENABLED = "enabled"
    DISABLED = "disabled"

    def visit(self, enabled: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1UpdateJitAccessConfigResponseAppliedSuccessfullyState.ENABLED:
            return enabled()
        if self is V1UpdateJitAccessConfigResponseAppliedSuccessfullyState.DISABLED:
            return disabled()
