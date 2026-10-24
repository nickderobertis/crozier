

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PilotAdsComponentReasonCode(enum.StrEnum):
    OPTIONAL_AMAZON_ADS_GATE_NOT_PASSED = "OPTIONAL_AMAZON_ADS_GATE_NOT_PASSED"

    def visit(self, optional_amazon_ads_gate_not_passed: typing.Callable[[], T_Result]) -> T_Result:
        if self is PilotAdsComponentReasonCode.OPTIONAL_AMAZON_ADS_GATE_NOT_PASSED:
            return optional_amazon_ads_gate_not_passed()
