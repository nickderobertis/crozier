

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AffiliateAttributionTouchpoint(enum.StrEnum):
    """
    Attribution touchpoint type. Use 'first' when capturing at session creation,
    'last' when capturing at completion. Enables multi-touch attribution models.
    """

    FIRST = "first"
    LAST = "last"

    def visit(self, first: typing.Callable[[], T_Result], last: typing.Callable[[], T_Result]) -> T_Result:
        if self is AffiliateAttributionTouchpoint.FIRST:
            return first()
        if self is AffiliateAttributionTouchpoint.LAST:
            return last()
