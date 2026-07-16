

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LocationStatus(enum.StrEnum):
    """
    The status of the location, whether a location is active or inactive.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is LocationStatus.ACTIVE:
            return active()
        if self is LocationStatus.INACTIVE:
            return inactive()
