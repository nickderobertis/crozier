

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSpacesDetailedListV3RequestView(enum.StrEnum):
    TREND = "trend"
    PROJECTION = "projection"
    PERIODS = "periods"

    def visit(
        self,
        trend: typing.Callable[[], T_Result],
        projection: typing.Callable[[], T_Result],
        periods: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSpacesDetailedListV3RequestView.TREND:
            return trend()
        if self is GetSpacesDetailedListV3RequestView.PROJECTION:
            return projection()
        if self is GetSpacesDetailedListV3RequestView.PERIODS:
            return periods()
