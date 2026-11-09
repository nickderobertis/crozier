

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentScheme(enum.StrEnum):
    """
    Payment scheme. If not specified - the default in the region will be used (e.g. `SEPA_CREDIT_TRANSFER` for EU). Using unsupported values will result in a failed payment.

    `LOCAL_DEFAULT`: The default payment scheme for the selected market and currency will be used.

    `LOCAL_INSTANT`: The instant payment scheme for the selected market and currency will be used (if applicable). Fees may be applied by the institution. If the market does not support an Instant Scheme (e.g. Denmark), the default in the region will be used.

    `SEPA_CREDIT_TRANSFER`: The standard payment to a beneficiary within the SEPA area.

    `SEPA_CREDIT_TRANSFER_INSTANT`: Instant payment within the SEPA area. May involve additional fees and may not be available at some banks.
    """

    LOCAL_DEFAULT = "LOCAL_DEFAULT"
    LOCAL_INSTANT = "LOCAL_INSTANT"
    SEPA_CREDIT_TRANSFER = "SEPA_CREDIT_TRANSFER"
    SEPA_CREDIT_TRANSFER_INSTANT = "SEPA_CREDIT_TRANSFER_INSTANT"

    def visit(
        self,
        local_default: typing.Callable[[], T_Result],
        local_instant: typing.Callable[[], T_Result],
        sepa_credit_transfer: typing.Callable[[], T_Result],
        sepa_credit_transfer_instant: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentScheme.LOCAL_DEFAULT:
            return local_default()
        if self is PaymentScheme.LOCAL_INSTANT:
            return local_instant()
        if self is PaymentScheme.SEPA_CREDIT_TRANSFER:
            return sepa_credit_transfer()
        if self is PaymentScheme.SEPA_CREDIT_TRANSFER_INSTANT:
            return sepa_credit_transfer_instant()
