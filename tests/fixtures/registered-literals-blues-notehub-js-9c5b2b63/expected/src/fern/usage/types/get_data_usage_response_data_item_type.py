

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDataUsageResponseDataItemType(enum.StrEnum):
    """
    The type of connectivity
    """

    CELLULAR = "cellular"
    SATELLITE = "satellite"

    def visit(self, cellular: typing.Callable[[], T_Result], satellite: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDataUsageResponseDataItemType.CELLULAR:
            return cellular()
        if self is GetDataUsageResponseDataItemType.SATELLITE:
            return satellite()
