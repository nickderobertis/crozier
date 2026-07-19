

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PresenceState(enum.StrEnum):
    IN_AREA = "IN_AREA"
    OUT_OF_AREA = "OUT_OF_AREA"
    UNKNOWN = "UNKNOWN"
    INACTIVE = "INACTIVE"

    def visit(
        self,
        in_area: typing.Callable[[], T_Result],
        out_of_area: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PresenceState.IN_AREA:
            return in_area()
        if self is PresenceState.OUT_OF_AREA:
            return out_of_area()
        if self is PresenceState.UNKNOWN:
            return unknown()
        if self is PresenceState.INACTIVE:
            return inactive()
