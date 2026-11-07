

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MandateResponseStatus(enum.StrEnum):
    """
    Current lifecycle status of the mandate.
    """

    ACTIVE = "active"
    INACTIVE = "inactive"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is MandateResponseStatus.ACTIVE:
            return active()
        if self is MandateResponseStatus.INACTIVE:
            return inactive()
