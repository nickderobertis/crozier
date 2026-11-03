

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PlotRequestBerthsItem(enum.StrEnum):
    QUAY_NORTH = "quay-north"
    QUAY_SOUTH = "quay-south"
    MOORING_BUOY = "mooring-buoy"

    def visit(
        self,
        quay_north: typing.Callable[[], T_Result],
        quay_south: typing.Callable[[], T_Result],
        mooring_buoy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlotRequestBerthsItem.QUAY_NORTH:
            return quay_north()
        if self is PlotRequestBerthsItem.QUAY_SOUTH:
            return quay_south()
        if self is PlotRequestBerthsItem.MOORING_BUOY:
            return mooring_buoy()
