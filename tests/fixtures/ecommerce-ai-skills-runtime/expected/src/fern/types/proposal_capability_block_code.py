

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProposalCapabilityBlockCode(enum.StrEnum):
    CONNECTOR_CAPABILITY_UNAVAILABLE = "CONNECTOR_CAPABILITY_UNAVAILABLE"
    AMAZON_ADS_CAPABILITY_UNAVAILABLE = "AMAZON_ADS_CAPABILITY_UNAVAILABLE"

    def visit(
        self,
        connector_capability_unavailable: typing.Callable[[], T_Result],
        amazon_ads_capability_unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProposalCapabilityBlockCode.CONNECTOR_CAPABILITY_UNAVAILABLE:
            return connector_capability_unavailable()
        if self is ProposalCapabilityBlockCode.AMAZON_ADS_CAPABILITY_UNAVAILABLE:
            return amazon_ads_capability_unavailable()
