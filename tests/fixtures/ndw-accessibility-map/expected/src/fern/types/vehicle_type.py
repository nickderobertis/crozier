

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VehicleType(enum.StrEnum):
    """
    Vehicle type
    """

    BUS = "bus"
    CAR = "car"
    LIGHT_COMMERCIAL_VEHICLE = "light_commercial_vehicle"
    MOTORCYCLE = "motorcycle"
    TRACTOR = "tractor"
    TRUCK = "truck"

    def visit(
        self,
        bus: typing.Callable[[], T_Result],
        car: typing.Callable[[], T_Result],
        light_commercial_vehicle: typing.Callable[[], T_Result],
        motorcycle: typing.Callable[[], T_Result],
        tractor: typing.Callable[[], T_Result],
        truck: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VehicleType.BUS:
            return bus()
        if self is VehicleType.CAR:
            return car()
        if self is VehicleType.LIGHT_COMMERCIAL_VEHICLE:
            return light_commercial_vehicle()
        if self is VehicleType.MOTORCYCLE:
            return motorcycle()
        if self is VehicleType.TRACTOR:
            return tractor()
        if self is VehicleType.TRUCK:
            return truck()
