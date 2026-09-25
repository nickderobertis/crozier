

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VehicleDetailResponseType(enum.StrEnum):
    INVENTORY_VEHICLE_RESPONSE = "inventory.vehicle.response"

    def visit(self, inventory_vehicle_response: typing.Callable[[], T_Result]) -> T_Result:
        if self is VehicleDetailResponseType.INVENTORY_VEHICLE_RESPONSE:
            return inventory_vehicle_response()
