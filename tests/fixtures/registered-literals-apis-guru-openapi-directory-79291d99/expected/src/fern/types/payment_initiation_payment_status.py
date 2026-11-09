

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentInitiationPaymentStatus(enum.StrEnum):
    """
    The status of the payment.

    `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.

    `PAYMENT_STATUS_INITIATED`: The payment has been successfully authorised and accepted by the financial institution but has not been executed.

    `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.

    `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.

    `PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.

    `PAYMENT_STATUS_AUTHORISING`: The payment is currently being processed. The payment will automatically exit this state when the financial institution has authorised the transaction.

    `PAYMENT_STATUS_CANCELLED`: The payment was cancelled during authorisation.

    `PAYMENT_STATUS_EXECUTED`: The payment has been successfully executed and is considered complete.

    `PAYMENT_STATUS_SETTLED`: The payment has settled and funds are available for use. Payment settlement can only be guaranteed by using Plaid virtual accounts. A payment will typically settle within seconds to several days, depending on which payment rail is used.

    `PAYMENT_STATUS_ESTABLISHED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.

    `PAYMENT_STATUS_REJECTED`: The payment was rejected by the financial institution.

    Deprecated:
    These statuses will be removed in a future release.

    `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.

    `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.

    `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.
    """

    PAYMENT_STATUS_INPUT_NEEDED = "PAYMENT_STATUS_INPUT_NEEDED"
    PAYMENT_STATUS_PROCESSING = "PAYMENT_STATUS_PROCESSING"
    PAYMENT_STATUS_INITIATED = "PAYMENT_STATUS_INITIATED"
    PAYMENT_STATUS_COMPLETED = "PAYMENT_STATUS_COMPLETED"
    PAYMENT_STATUS_INSUFFICIENT_FUNDS = "PAYMENT_STATUS_INSUFFICIENT_FUNDS"
    PAYMENT_STATUS_FAILED = "PAYMENT_STATUS_FAILED"
    PAYMENT_STATUS_BLOCKED = "PAYMENT_STATUS_BLOCKED"
    PAYMENT_STATUS_UNKNOWN = "PAYMENT_STATUS_UNKNOWN"
    PAYMENT_STATUS_EXECUTED = "PAYMENT_STATUS_EXECUTED"
    PAYMENT_STATUS_SETTLED = "PAYMENT_STATUS_SETTLED"
    PAYMENT_STATUS_AUTHORISING = "PAYMENT_STATUS_AUTHORISING"
    PAYMENT_STATUS_CANCELLED = "PAYMENT_STATUS_CANCELLED"
    PAYMENT_STATUS_ESTABLISHED = "PAYMENT_STATUS_ESTABLISHED"
    PAYMENT_STATUS_REJECTED = "PAYMENT_STATUS_REJECTED"

    def visit(
        self,
        payment_status_input_needed: typing.Callable[[], T_Result],
        payment_status_processing: typing.Callable[[], T_Result],
        payment_status_initiated: typing.Callable[[], T_Result],
        payment_status_completed: typing.Callable[[], T_Result],
        payment_status_insufficient_funds: typing.Callable[[], T_Result],
        payment_status_failed: typing.Callable[[], T_Result],
        payment_status_blocked: typing.Callable[[], T_Result],
        payment_status_unknown: typing.Callable[[], T_Result],
        payment_status_executed: typing.Callable[[], T_Result],
        payment_status_settled: typing.Callable[[], T_Result],
        payment_status_authorising: typing.Callable[[], T_Result],
        payment_status_cancelled: typing.Callable[[], T_Result],
        payment_status_established: typing.Callable[[], T_Result],
        payment_status_rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_INPUT_NEEDED:
            return payment_status_input_needed()
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_PROCESSING:
            return payment_status_processing()
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_INITIATED:
            return payment_status_initiated()
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_COMPLETED:
            return payment_status_completed()
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_INSUFFICIENT_FUNDS:
            return payment_status_insufficient_funds()
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_FAILED:
            return payment_status_failed()
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_BLOCKED:
            return payment_status_blocked()
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_UNKNOWN:
            return payment_status_unknown()
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_EXECUTED:
            return payment_status_executed()
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_SETTLED:
            return payment_status_settled()
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_AUTHORISING:
            return payment_status_authorising()
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_CANCELLED:
            return payment_status_cancelled()
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_ESTABLISHED:
            return payment_status_established()
        if self is PaymentInitiationPaymentStatus.PAYMENT_STATUS_REJECTED:
            return payment_status_rejected()
