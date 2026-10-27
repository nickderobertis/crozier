

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Tone(enum.StrEnum):
    """
    How the sensor's alarm sounds.
    """

    CHIME = "chime"
    BUZZ = "buzz"

    def visit(self, chime: typing.Callable[[], T_Result], buzz: typing.Callable[[], T_Result]) -> T_Result:
        if self is Tone.CHIME:
            return chime()
        if self is Tone.BUZZ:
            return buzz()
