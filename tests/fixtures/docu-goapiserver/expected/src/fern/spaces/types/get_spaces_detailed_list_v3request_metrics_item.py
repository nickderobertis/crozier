

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSpacesDetailedListV3RequestMetricsItem(enum.StrEnum):
    SUM_AVAILABLE_SPACES = "sum_available_spaces"
    SUM_OPEN_SPACES = "sum_open_spaces"
    SUM_OCCUPIED_SPACES = "sum_occupied_spaces"
    SUM_CLOSED_SPACES = "sum_closed_spaces"
    SUM_UNAVAILABLE_SPACES = "sum_unavailable_spaces"
    CAPACITY = "capacity"
    OCCUPANCY_RATE = "occupancy_rate"

    def visit(
        self,
        sum_available_spaces: typing.Callable[[], T_Result],
        sum_open_spaces: typing.Callable[[], T_Result],
        sum_occupied_spaces: typing.Callable[[], T_Result],
        sum_closed_spaces: typing.Callable[[], T_Result],
        sum_unavailable_spaces: typing.Callable[[], T_Result],
        capacity: typing.Callable[[], T_Result],
        occupancy_rate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSpacesDetailedListV3RequestMetricsItem.SUM_AVAILABLE_SPACES:
            return sum_available_spaces()
        if self is GetSpacesDetailedListV3RequestMetricsItem.SUM_OPEN_SPACES:
            return sum_open_spaces()
        if self is GetSpacesDetailedListV3RequestMetricsItem.SUM_OCCUPIED_SPACES:
            return sum_occupied_spaces()
        if self is GetSpacesDetailedListV3RequestMetricsItem.SUM_CLOSED_SPACES:
            return sum_closed_spaces()
        if self is GetSpacesDetailedListV3RequestMetricsItem.SUM_UNAVAILABLE_SPACES:
            return sum_unavailable_spaces()
        if self is GetSpacesDetailedListV3RequestMetricsItem.CAPACITY:
            return capacity()
        if self is GetSpacesDetailedListV3RequestMetricsItem.OCCUPANCY_RATE:
            return occupancy_rate()
