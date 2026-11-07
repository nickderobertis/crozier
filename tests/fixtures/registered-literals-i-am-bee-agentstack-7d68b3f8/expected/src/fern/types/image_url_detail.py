

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImageUrlDetail(enum.StrEnum):
    AUTO = "auto"
    LOW = "low"
    HIGH = "high"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ImageUrlDetail.AUTO:
            return auto()
        if self is ImageUrlDetail.LOW:
            return low()
        if self is ImageUrlDetail.HIGH:
            return high()
