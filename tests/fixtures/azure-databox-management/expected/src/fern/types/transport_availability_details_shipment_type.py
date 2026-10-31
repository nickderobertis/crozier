

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransportAvailabilityDetailsShipmentType(enum.StrEnum):
    """
    Transport Shipment Type supported for given region.
    """

    CUSTOMER_MANAGED = "CustomerManaged"
    MICROSOFT_MANAGED = "MicrosoftManaged"

    def visit(
        self, customer_managed: typing.Callable[[], T_Result], microsoft_managed: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TransportAvailabilityDetailsShipmentType.CUSTOMER_MANAGED:
            return customer_managed()
        if self is TransportAvailabilityDetailsShipmentType.MICROSOFT_MANAGED:
            return microsoft_managed()
