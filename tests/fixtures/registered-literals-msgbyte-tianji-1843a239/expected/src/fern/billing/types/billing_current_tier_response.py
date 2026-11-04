

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class BillingCurrentTierResponse(enum.StrEnum):
    FREE = "FREE"
    PRO = "PRO"
    TEAM = "TEAM"
    UNLIMITED = "UNLIMITED"

    def visit(
        self,
        free: typing.Callable[[], T_Result],
        pro: typing.Callable[[], T_Result],
        team: typing.Callable[[], T_Result],
        unlimited: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BillingCurrentTierResponse.FREE:
            return free()
        if self is BillingCurrentTierResponse.PRO:
            return pro()
        if self is BillingCurrentTierResponse.TEAM:
            return team()
        if self is BillingCurrentTierResponse.UNLIMITED:
            return unlimited()
