

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class InstallPluginRequestSource(enum.StrEnum):
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
        if self is InstallPluginRequestSource.FILE:
            return file()
        if self is InstallPluginRequestSource.PRESET:
            return preset()
        if self is InstallPluginRequestSource.URL:
            return url()
