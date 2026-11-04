

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UiPluginProviderType(enum.StrEnum):
    PLUGIN = "plugin"
    THEME = "theme"

    def visit(self, plugin: typing.Callable[[], T_Result], theme: typing.Callable[[], T_Result]) -> T_Result:
        if self is UiPluginProviderType.PLUGIN:
            return plugin()
        if self is UiPluginProviderType.THEME:
            return theme()
