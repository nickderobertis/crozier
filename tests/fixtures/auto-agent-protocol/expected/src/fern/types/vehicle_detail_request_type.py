

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VehicleDetailRequestType(enum.StrEnum):
    INVENTORY_VEHICLE_REQUEST = "inventory.vehicle.request"

    def visit(self, inventory_vehicle_request: typing.Callable[[], T_Result]) -> T_Result:
        if self is VehicleDetailRequestType.INVENTORY_VEHICLE_REQUEST:
            return inventory_vehicle_request()
