

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadShapeType(enum.StrEnum):
    """
    named load shape: SPIKE (ramp up, hold the peak, ramp back down, optional recovery hold); STAIRS (a flight of pure-hold steps, each one 'step' higher); RAMP_HOLD (ramp 0 to target then hold).
    """

    SPIKE = "SPIKE"
    STAIRS = "STAIRS"
    RAMP_HOLD = "RAMP_HOLD"

    def visit(
        self,
        spike: typing.Callable[[], T_Result],
        stairs: typing.Callable[[], T_Result],
        ramp_hold: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoadShapeType.SPIKE:
            return spike()
        if self is LoadShapeType.STAIRS:
            return stairs()
        if self is LoadShapeType.RAMP_HOLD:
            return ramp_hold()
