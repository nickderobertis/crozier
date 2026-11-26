

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParcelState(enum.StrEnum):
    """
    Where a parcel is in its journey.
    """

    DRAFTED = "drafted"
    STAMPED = "stamped"
    DELIVERED = "delivered"

    def visit(
        self,
        drafted: typing.Callable[[], T_Result],
        stamped: typing.Callable[[], T_Result],
        delivered: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParcelState.DRAFTED:
            return drafted()
        if self is ParcelState.STAMPED:
            return stamped()
        if self is ParcelState.DELIVERED:
            return delivered()
