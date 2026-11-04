

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MeGetResponseTier(enum.StrEnum):
    """
    Your account tier
    """

    FREE = "free"
    PRO = "pro"
    BUSINESS = "business"

    def visit(
        self,
        free: typing.Callable[[], T_Result],
        pro: typing.Callable[[], T_Result],
        business: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MeGetResponseTier.FREE:
            return free()
        if self is MeGetResponseTier.PRO:
            return pro()
        if self is MeGetResponseTier.BUSINESS:
            return business()
