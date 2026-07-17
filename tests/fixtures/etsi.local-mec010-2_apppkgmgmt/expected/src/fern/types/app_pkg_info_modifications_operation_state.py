

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppPkgInfoModificationsOperationState(enum.StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"

    def visit(self, disabled: typing.Callable[[], T_Result], enabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is AppPkgInfoModificationsOperationState.DISABLED:
            return disabled()
        if self is AppPkgInfoModificationsOperationState.ENABLED:
            return enabled()
