

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CableStatusLabel(enum.StrEnum):
    CONNECTED = "Connected"
    PLANNED = "Planned"
    DECOMMISSIONING = "Decommissioning"

    def visit(
        self,
        connected: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        decommissioning: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CableStatusLabel.CONNECTED:
            return connected()
        if self is CableStatusLabel.PLANNED:
            return planned()
        if self is CableStatusLabel.DECOMMISSIONING:
            return decommissioning()
