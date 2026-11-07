

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CountdownBarInputProgressFill(enum.StrEnum):
    """
    Background treatment behind the bar text. "drain" starts the bar fully tinted when the lead window opens and retreats the tint leftward as the target approaches, leaving only the bar background at zero. Omitted means "none".
    """

    NONE = "none"
    DRAIN = "drain"

    def visit(self, none: typing.Callable[[], T_Result], drain: typing.Callable[[], T_Result]) -> T_Result:
        if self is CountdownBarInputProgressFill.NONE:
            return none()
        if self is CountdownBarInputProgressFill.DRAIN:
            return drain()
