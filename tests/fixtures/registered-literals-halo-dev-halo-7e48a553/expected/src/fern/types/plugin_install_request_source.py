

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PluginInstallRequestSource(enum.StrEnum):
    """
    Install source. Defaults to file.
    """

    FILE = "FILE"
    PRESET = "PRESET"
    URL = "URL"

    def visit(
        self,
        file: typing.Callable[[], T_Result],
        preset: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PluginInstallRequestSource.FILE:
            return file()
        if self is PluginInstallRequestSource.PRESET:
            return preset()
        if self is PluginInstallRequestSource.URL:
            return url()
