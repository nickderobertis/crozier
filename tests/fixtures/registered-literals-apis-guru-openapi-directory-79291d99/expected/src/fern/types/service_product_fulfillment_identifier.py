

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceProductFulfillmentIdentifier(enum.StrEnum):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    VOA = "VOA"
    VOETRANSACTIONS = "VOETRANSACTIONS"

    def visit(self, voa: typing.Callable[[], T_Result], voetransactions: typing.Callable[[], T_Result]) -> T_Result:
        if self is ServiceProductFulfillmentIdentifier.VOA:
            return voa()
        if self is ServiceProductFulfillmentIdentifier.VOETRANSACTIONS:
            return voetransactions()
