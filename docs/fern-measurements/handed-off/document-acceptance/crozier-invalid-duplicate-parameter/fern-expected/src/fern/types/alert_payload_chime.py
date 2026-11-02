

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertPayloadChime(enum.StrEnum):
    CLASSIC = "classic"
    SOFT = "soft"

    def visit(self, classic: typing.Callable[[], T_Result], soft: typing.Callable[[], T_Result]) -> T_Result:
        if self is AlertPayloadChime.CLASSIC:
            return classic()
        if self is AlertPayloadChime.SOFT:
            return soft()
