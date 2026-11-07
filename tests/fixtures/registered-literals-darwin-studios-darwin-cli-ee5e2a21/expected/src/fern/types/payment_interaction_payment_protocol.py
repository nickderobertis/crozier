

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentInteractionPaymentProtocol(enum.StrEnum):
    DARWIN_WALLET = "DARWIN_WALLET"
    HOSTED_CHECKOUT = "HOSTED_CHECKOUT"
    UCP_SPT = "UCP_SPT"
    ACP_SPT = "ACP_SPT"
    MPP_SPT = "MPP_SPT"
    X402 = "X402"

    def visit(
        self,
        darwin_wallet: typing.Callable[[], T_Result],
        hosted_checkout: typing.Callable[[], T_Result],
        ucp_spt: typing.Callable[[], T_Result],
        acp_spt: typing.Callable[[], T_Result],
        mpp_spt: typing.Callable[[], T_Result],
        x402: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentInteractionPaymentProtocol.DARWIN_WALLET:
            return darwin_wallet()
        if self is PaymentInteractionPaymentProtocol.HOSTED_CHECKOUT:
            return hosted_checkout()
        if self is PaymentInteractionPaymentProtocol.UCP_SPT:
            return ucp_spt()
        if self is PaymentInteractionPaymentProtocol.ACP_SPT:
            return acp_spt()
        if self is PaymentInteractionPaymentProtocol.MPP_SPT:
            return mpp_spt()
        if self is PaymentInteractionPaymentProtocol.X402:
            return x402()
