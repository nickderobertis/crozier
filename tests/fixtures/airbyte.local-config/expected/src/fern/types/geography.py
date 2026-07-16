

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Geography(enum.StrEnum):
    AUTO = "auto"
    US = "us"
    EU = "eu"

    def visit(
        self, auto: typing.Callable[[], T_Result], us: typing.Callable[[], T_Result], eu: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is Geography.AUTO:
            return auto()
        if self is Geography.US:
            return us()
        if self is Geography.EU:
            return eu()
