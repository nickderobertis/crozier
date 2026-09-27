

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlatformStatus(enum.StrEnum):
    ACTIVE = "active"
    COMING_SOON = "coming_soon"
    OAUTH_NOT_CONFIGURED = "oauth_not_configured"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        coming_soon: typing.Callable[[], T_Result],
        oauth_not_configured: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlatformStatus.ACTIVE:
            return active()
        if self is PlatformStatus.COMING_SOON:
            return coming_soon()
        if self is PlatformStatus.OAUTH_NOT_CONFIGURED:
            return oauth_not_configured()
