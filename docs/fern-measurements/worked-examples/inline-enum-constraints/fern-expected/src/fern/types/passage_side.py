

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PassageSide(enum.StrEnum):
    """
    No member satisfies the pattern, so the first stands.
    """

    PORT = "port"
    STARBOARD = "starboard"

    def visit(self, port: typing.Callable[[], T_Result], starboard: typing.Callable[[], T_Result]) -> T_Result:
        if self is PassageSide.PORT:
            return port()
        if self is PassageSide.STARBOARD:
            return starboard()
