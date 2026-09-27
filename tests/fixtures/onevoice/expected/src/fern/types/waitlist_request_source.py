

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WaitlistRequestSource(enum.StrEnum):
    """
    Optional latest signup source; omitted values preserve existing attribution.
    """

    LANDING = "landing"
    BILLING = "billing"
    BUSINESS_LIMIT = "business-limit"

    def visit(
        self,
        landing: typing.Callable[[], T_Result],
        billing: typing.Callable[[], T_Result],
        business_limit: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WaitlistRequestSource.LANDING:
            return landing()
        if self is WaitlistRequestSource.BILLING:
            return billing()
        if self is WaitlistRequestSource.BUSINESS_LIMIT:
            return business_limit()
