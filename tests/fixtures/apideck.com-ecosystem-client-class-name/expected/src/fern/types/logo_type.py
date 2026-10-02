

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LogoType(enum.StrEnum):
    LOGO = "LOGO"
    BANNER = "BANNER"
    SCREENSHOT = "SCREENSHOT"

    def visit(
        self,
        logo: typing.Callable[[], T_Result],
        banner: typing.Callable[[], T_Result],
        screenshot: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LogoType.LOGO:
            return logo()
        if self is LogoType.BANNER:
            return banner()
        if self is LogoType.SCREENSHOT:
            return screenshot()
