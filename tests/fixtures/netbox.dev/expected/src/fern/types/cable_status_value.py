

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CableStatusValue(str, enum.Enum):
    CONNECTED = "connected"
    PLANNED = "planned"
    DECOMMISSIONING = "decommissioning"

    def visit(
        self,
        connected: typing.Callable[[], T_Result],
        planned: typing.Callable[[], T_Result],
        decommissioning: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CableStatusValue.CONNECTED:
            return connected()
        if self is CableStatusValue.PLANNED:
            return planned()
        if self is CableStatusValue.DECOMMISSIONING:
            return decommissioning()
