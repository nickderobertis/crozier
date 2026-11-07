

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImageDetail(enum.StrEnum):
    LOW = "low"
    HIGH = "high"
    AUTO = "auto"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ImageDetail.LOW:
            return low()
        if self is ImageDetail.HIGH:
            return high()
        if self is ImageDetail.AUTO:
            return auto()
