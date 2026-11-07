

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CapabilityPaymentRequirementHandlersItem(enum.StrEnum):
    HOSTED_CHECKOUT = "HOSTED_CHECKOUT"
    UCP_SPT = "UCP_SPT"
    ACP_SPT = "ACP_SPT"
    MPP_SPT = "MPP_SPT"
    X402 = "X402"

    def visit(
        self,
        hosted_checkout: typing.Callable[[], T_Result],
        ucp_spt: typing.Callable[[], T_Result],
        acp_spt: typing.Callable[[], T_Result],
        mpp_spt: typing.Callable[[], T_Result],
        x402: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CapabilityPaymentRequirementHandlersItem.HOSTED_CHECKOUT:
            return hosted_checkout()
        if self is CapabilityPaymentRequirementHandlersItem.UCP_SPT:
            return ucp_spt()
        if self is CapabilityPaymentRequirementHandlersItem.ACP_SPT:
            return acp_spt()
        if self is CapabilityPaymentRequirementHandlersItem.MPP_SPT:
            return mpp_spt()
        if self is CapabilityPaymentRequirementHandlersItem.X402:
            return x402()
