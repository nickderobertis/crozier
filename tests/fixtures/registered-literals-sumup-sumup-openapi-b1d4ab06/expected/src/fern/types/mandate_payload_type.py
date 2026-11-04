

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MandatePayloadType(enum.StrEnum):
    """
    Type of mandate to create for the saved payment instrument.
    """

    RECURRENT = "recurrent"

    def visit(self, recurrent: typing.Callable[[], T_Result]) -> T_Result:
        if self is MandatePayloadType.RECURRENT:
            return recurrent()
