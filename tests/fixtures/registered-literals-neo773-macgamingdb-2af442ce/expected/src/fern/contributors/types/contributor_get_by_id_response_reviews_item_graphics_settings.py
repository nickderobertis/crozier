

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ContributorGetByIdResponseReviewsItemGraphicsSettings(enum.StrEnum):
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
        if self is ContributorGetByIdResponseReviewsItemGraphicsSettings.ULTRA:
            return ultra()
        if self is ContributorGetByIdResponseReviewsItemGraphicsSettings.HIGH:
            return high()
        if self is ContributorGetByIdResponseReviewsItemGraphicsSettings.MEDIUM:
            return medium()
        if self is ContributorGetByIdResponseReviewsItemGraphicsSettings.LOW:
            return low()
