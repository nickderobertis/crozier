

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WirelessLinkStatusLabel(enum.StrEnum):
    CONNECTED = "Connected"
    PLANNED = "Planned"
    DECOMMISSIONING = "Decommissioning"

    def visit(
        self,
        connected: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        decommissioning: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WirelessLinkStatusLabel.CONNECTED:
            return connected()
        if self is WirelessLinkStatusLabel.PLANNED:
            return planned()
        if self is WirelessLinkStatusLabel.DECOMMISSIONING:
            return decommissioning()
