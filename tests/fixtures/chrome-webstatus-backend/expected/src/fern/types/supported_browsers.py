

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SupportedBrowsers(enum.StrEnum):
    """
    List of supported browsers that webstatus.dev currently ingests
    """

    CHROME = "chrome"
    FIREFOX = "firefox"
    SAFARI = "safari"
    EDGE = "edge"
    CHROME_ANDROID = "chrome_android"
    FIREFOX_ANDROID = "firefox_android"
    SAFARI_IOS = "safari_ios"

    def visit(
        self,
        chrome: typing.Callable[[], T_Result],
        firefox: typing.Callable[[], T_Result],
        safari: typing.Callable[[], T_Result],
        edge: typing.Callable[[], T_Result],
        chrome_android: typing.Callable[[], T_Result],
        firefox_android: typing.Callable[[], T_Result],
        safari_ios: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SupportedBrowsers.CHROME:
            return chrome()
        if self is SupportedBrowsers.FIREFOX:
            return firefox()
        if self is SupportedBrowsers.SAFARI:
            return safari()
        if self is SupportedBrowsers.EDGE:
            return edge()
        if self is SupportedBrowsers.CHROME_ANDROID:
            return chrome_android()
        if self is SupportedBrowsers.FIREFOX_ANDROID:
            return firefox_android()
        if self is SupportedBrowsers.SAFARI_IOS:
            return safari_ios()
