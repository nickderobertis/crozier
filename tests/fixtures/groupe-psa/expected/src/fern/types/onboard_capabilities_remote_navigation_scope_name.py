

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OnboardCapabilitiesRemoteNavigationScopeName(enum.StrEnum):
    REMOTE_NAVIGATION_WRITE = "remote:navigation:write"

    def visit(self, remote_navigation_write: typing.Callable[[], T_Result]) -> T_Result:
        if self is OnboardCapabilitiesRemoteNavigationScopeName.REMOTE_NAVIGATION_WRITE:
            return remote_navigation_write()
