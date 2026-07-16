

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MediaType(str, enum.Enum):
    SCREENSHOT = "SCREENSHOT"
    VIDEO = "VIDEO"

    def visit(self, screenshot: typing.Callable[[], T_Result], video: typing.Callable[[], T_Result]) -> T_Result:
        if self is MediaType.SCREENSHOT:
            return screenshot()
        if self is MediaType.VIDEO:
            return video()
