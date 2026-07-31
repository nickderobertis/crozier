

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BrandVettingEnumVettingProvider(enum.StrEnum):
    CAMPAIGN_VERIFY = "campaign-verify"

    def visit(self, campaign_verify: typing.Callable[[], T_Result]) -> T_Result:
        if self is BrandVettingEnumVettingProvider.CAMPAIGN_VERIFY:
            return campaign_verify()
