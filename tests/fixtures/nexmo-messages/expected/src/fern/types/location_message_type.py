

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LocationMessageType(enum.StrEnum):
    """
    The type of message to send. You must provide `location` in this field
    """

    LOCATION = "location"

    def visit(self, location: typing.Callable[[], T_Result]) -> T_Result:
        if self is LocationMessageType.LOCATION:
            return location()
