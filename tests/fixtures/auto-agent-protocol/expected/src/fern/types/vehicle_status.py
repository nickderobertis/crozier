

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VehicleStatus(enum.StrEnum):
    """
    Inventory availability. v1.0 supports exactly three values: `available` (in stock now), `intransit` (allocated / en route to the dealership), `pending` (deal in progress). A vehicle in any other state is OUT OF STOCK and MUST NOT appear in inventory feeds — dealers omit it and buyer agents ignore any item missing or carrying an unknown status. Required on inventory listings; omitted on vehicle_of_interest and trade_in.
    """

    AVAILABLE = "available"
    INTRANSIT = "intransit"
    PENDING = "pending"

    def visit(
        self,
        available: typing.Callable[[], T_Result],
        intransit: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VehicleStatus.AVAILABLE:
            return available()
        if self is VehicleStatus.INTRANSIT:
            return intransit()
        if self is VehicleStatus.PENDING:
            return pending()
