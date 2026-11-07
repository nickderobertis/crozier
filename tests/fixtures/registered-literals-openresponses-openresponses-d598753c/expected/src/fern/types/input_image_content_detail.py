

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InputImageContentDetail(enum.StrEnum):
    """
    The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.
    """

    LOW = "low"
    HIGH = "high"
    AUTO = "auto"

    def visit(
        self,
        low: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InputImageContentDetail.LOW:
            return low()
        if self is InputImageContentDetail.HIGH:
            return high()
        if self is InputImageContentDetail.AUTO:
            return auto()
