

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WirelessLinkStatusValue(enum.StrEnum):
    CONNECTED = "connected"
    PLANNED = "planned"
    DECOMMISSIONING = "decommissioning"

    def visit(
        self,
        connected: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        decommissioning: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WirelessLinkStatusValue.CONNECTED:
            return connected()
        if self is WirelessLinkStatusValue.PLANNED:
            return planned()
        if self is WirelessLinkStatusValue.DECOMMISSIONING:
            return decommissioning()
