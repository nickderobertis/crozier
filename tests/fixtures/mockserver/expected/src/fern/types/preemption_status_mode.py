

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreemptionStatusMode(enum.StrEnum):
    """
    active signalling mode (omitted when inactive)
    """

    REJECT503 = "reject503"
    GOAWAY = "goaway"
    BOTH = "both"

    def visit(
        self,
        reject503: typing.Callable[[], T_Result],
        goaway: typing.Callable[[], T_Result],
        both: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PreemptionStatusMode.REJECT503:
            return reject503()
        if self is PreemptionStatusMode.GOAWAY:
            return goaway()
        if self is PreemptionStatusMode.BOTH:
            return both()
