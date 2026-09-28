

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NamespacesGetError503ErrorCode(enum.StrEnum):
    PLUGIN_UNAVAILABLE = "PLUGIN_UNAVAILABLE"

    def visit(self, plugin_unavailable: typing.Callable[[], T_Result]) -> T_Result:
        if self is NamespacesGetError503ErrorCode.PLUGIN_UNAVAILABLE:
            return plugin_unavailable()
