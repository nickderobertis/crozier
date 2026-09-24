

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V60OriginDestinationValue(enum.StrEnum):
    """
    Sourcing basis for the location: 'O' = origin-based (ship-from rate), 'D' = destination-based (ship-to rate).
    """

    O = "O"
    D = "D"

    def visit(self, o: typing.Callable[[], T_Result], d: typing.Callable[[], T_Result]) -> T_Result:
        if self is V60OriginDestinationValue.O:
            return o()
        if self is V60OriginDestinationValue.D:
            return d()
