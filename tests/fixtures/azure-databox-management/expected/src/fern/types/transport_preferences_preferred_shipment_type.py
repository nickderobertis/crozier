

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransportPreferencesPreferredShipmentType(enum.StrEnum):
    """
    Indicates Shipment Logistics type that the customer preferred.
    """

    CUSTOMER_MANAGED = "CustomerManaged"
    MICROSOFT_MANAGED = "MicrosoftManaged"

    def visit(
        self, customer_managed: typing.Callable[[], T_Result], microsoft_managed: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TransportPreferencesPreferredShipmentType.CUSTOMER_MANAGED:
            return customer_managed()
        if self is TransportPreferencesPreferredShipmentType.MICROSOFT_MANAGED:
            return microsoft_managed()
