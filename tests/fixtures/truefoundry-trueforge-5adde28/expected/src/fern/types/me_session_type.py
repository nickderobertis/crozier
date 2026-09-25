

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MeSessionType(enum.StrEnum):
    """
    `oidc-connected` when the process is running with browser OIDC login; `default` for standalone or TrueFoundry token auth.
    """

    DEFAULT = "default"
    OIDC_CONNECTED = "oidc-connected"

    def visit(self, default: typing.Callable[[], T_Result], oidc_connected: typing.Callable[[], T_Result]) -> T_Result:
        if self is MeSessionType.DEFAULT:
            return default()
        if self is MeSessionType.OIDC_CONNECTED:
            return oidc_connected()
