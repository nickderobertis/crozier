

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ForbiddenErrorBodyCode(enum.StrEnum):
    """
    Machine-readable denial code, present when the 403 is a billing-provider-confirmed subscription lapse (mirrored in the X-Billing-Verification response header).
    """

    SUBSCRIPTION_LAPSED = "subscription_lapsed"

    def visit(self, subscription_lapsed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ForbiddenErrorBodyCode.SUBSCRIPTION_LAPSED:
            return subscription_lapsed()
