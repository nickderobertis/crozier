

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImageUrlsInfo(enum.StrEnum):
    STORED = "STORED"

    def visit(self, stored: typing.Callable[[], T_Result]) -> T_Result:
        if self is ImageUrlsInfo.STORED:
            return stored()
