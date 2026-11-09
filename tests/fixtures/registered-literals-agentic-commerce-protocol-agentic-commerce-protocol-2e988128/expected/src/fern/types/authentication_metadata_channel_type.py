

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationMetadataChannelType(enum.StrEnum):
    """
    Use "browser" to indicate the transaction originated from a browser.
    """

    BROWSER = "browser"

    def visit(self, browser: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthenticationMetadataChannelType.BROWSER:
            return browser()
