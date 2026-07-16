

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FileType(str, enum.Enum):
    LOGO = "LOGO"
    BANNER = "BANNER"
    SCREENSHOT = "SCREENSHOT"

    def visit(
        self,
        logo: typing.Callable[[], T_Result],
        banner: typing.Callable[[], T_Result],
        screenshot: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileType.LOGO:
            return logo()
        if self is FileType.BANNER:
            return banner()
        if self is FileType.SCREENSHOT:
            return screenshot()
