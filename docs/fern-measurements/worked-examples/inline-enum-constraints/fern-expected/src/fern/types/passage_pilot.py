

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PassagePilot(enum.StrEnum):
    """
    A format no member is decided against, so the first stands.
    """

    HARBOUR = "harbour"
    SEA = "sea"

    def visit(self, harbour: typing.Callable[[], T_Result], sea: typing.Callable[[], T_Result]) -> T_Result:
        if self is PassagePilot.HARBOUR:
            return harbour()
        if self is PassagePilot.SEA:
            return sea()
