

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OrderFulfillmentType(enum.StrEnum):
    """
    The type of fulfillment.
    """

    PICKUP = "PICKUP"
    SHIPMENT = "SHIPMENT"

    def visit(self, pickup: typing.Callable[[], T_Result], shipment: typing.Callable[[], T_Result]) -> T_Result:
        if self is OrderFulfillmentType.PICKUP:
            return pickup()
        if self is OrderFulfillmentType.SHIPMENT:
            return shipment()
