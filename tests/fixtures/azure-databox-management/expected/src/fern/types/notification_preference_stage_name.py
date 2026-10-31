

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationPreferenceStageName(enum.StrEnum):
    """
    Name of the stage.
    """

    DEVICE_PREPARED = "DevicePrepared"
    DISPATCHED = "Dispatched"
    DELIVERED = "Delivered"
    PICKED_UP = "PickedUp"
    AT_AZURE_DC = "AtAzureDC"
    DATA_COPY = "DataCopy"

    def visit(
        self,
        device_prepared: typing.Callable[[], T_Result],
        dispatched: typing.Callable[[], T_Result],
        delivered: typing.Callable[[], T_Result],
        picked_up: typing.Callable[[], T_Result],
        at_azure_dc: typing.Callable[[], T_Result],
        data_copy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NotificationPreferenceStageName.DEVICE_PREPARED:
            return device_prepared()
        if self is NotificationPreferenceStageName.DISPATCHED:
            return dispatched()
        if self is NotificationPreferenceStageName.DELIVERED:
            return delivered()
        if self is NotificationPreferenceStageName.PICKED_UP:
            return picked_up()
        if self is NotificationPreferenceStageName.AT_AZURE_DC:
            return at_azure_dc()
        if self is NotificationPreferenceStageName.DATA_COPY:
            return data_copy()
