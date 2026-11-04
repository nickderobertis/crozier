

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PluginInUseErrorErrorCode(enum.StrEnum):
    PLUGIN_IN_USE = "plugin_in_use"

    def visit(self, plugin_in_use: typing.Callable[[], T_Result]) -> T_Result:
        if self is PluginInUseErrorErrorCode.PLUGIN_IN_USE:
            return plugin_in_use()
