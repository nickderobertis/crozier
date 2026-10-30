

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReadConsistency(enum.StrEnum):
    """
    How recently a live read confirms the namespace head, without a maximum
    staleness.

    A runtime's default consistency and the `consistency` field of a download
    request take one of these values. `eventual` reads at the head that was
    confirmed last while that confirmation is younger than the maximum
    staleness, and `strong` confirms the head before the read.
    """

    EVENTUAL = "eventual"
    STRONG = "strong"

    def visit(self, eventual: typing.Callable[[], T_Result], strong: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReadConsistency.EVENTUAL:
            return eventual()
        if self is ReadConsistency.STRONG:
            return strong()
