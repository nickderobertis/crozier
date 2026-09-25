

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BeltStatusId(enum.StrEnum):
    """
    Seat identifier.
    """

    DRIVER = "Driver"
    PASSENGER = "Passenger"

    def visit(self, driver: typing.Callable[[], T_Result], passenger: typing.Callable[[], T_Result]) -> T_Result:
        if self is BeltStatusId.DRIVER:
            return driver()
        if self is BeltStatusId.PASSENGER:
            return passenger()
