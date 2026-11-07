

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PersistentBrowserType(enum.StrEnum):
    MSEDGE = "msedge"
    CHROME = "chrome"
    STEALTH_CHROMIUM = "stealth-chromium"

    def visit(
        self,
        msedge: typing.Callable[[], T_Result],
        chrome: typing.Callable[[], T_Result],
        stealth_chromium: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PersistentBrowserType.MSEDGE:
            return msedge()
        if self is PersistentBrowserType.CHROME:
            return chrome()
        if self is PersistentBrowserType.STEALTH_CHROMIUM:
            return stealth_chromium()
