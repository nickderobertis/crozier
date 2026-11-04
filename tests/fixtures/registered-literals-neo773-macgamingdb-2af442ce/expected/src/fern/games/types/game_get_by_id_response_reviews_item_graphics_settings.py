

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GameGetByIdResponseReviewsItemGraphicsSettings(enum.StrEnum):
    ULTRA = "ULTRA"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def visit(
        self,
        ultra: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GameGetByIdResponseReviewsItemGraphicsSettings.ULTRA:
            return ultra()
        if self is GameGetByIdResponseReviewsItemGraphicsSettings.HIGH:
            return high()
        if self is GameGetByIdResponseReviewsItemGraphicsSettings.MEDIUM:
            return medium()
        if self is GameGetByIdResponseReviewsItemGraphicsSettings.LOW:
            return low()
