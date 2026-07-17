

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ErrorCategory(enum.StrEnum):
    """
    Indicates which high-level category of error has occurred during a
    request to the Connect API.
    """

    API_ERROR = "API_ERROR"
    AUTHENTICATION_ERROR = "AUTHENTICATION_ERROR"
    INVALID_REQUEST_ERROR = "INVALID_REQUEST_ERROR"
    RATE_LIMIT_ERROR = "RATE_LIMIT_ERROR"
    PAYMENT_METHOD_ERROR = "PAYMENT_METHOD_ERROR"
    REFUND_ERROR = "REFUND_ERROR"
    MERCHANT_SUBSCRIPTION_ERROR = "MERCHANT_SUBSCRIPTION_ERROR"

    def visit(
        self,
        api_error: typing.Callable[[], T_Result],
        authentication_error: typing.Callable[[], T_Result],
        invalid_request_error: typing.Callable[[], T_Result],
        rate_limit_error: typing.Callable[[], T_Result],
        payment_method_error: typing.Callable[[], T_Result],
        refund_error: typing.Callable[[], T_Result],
        merchant_subscription_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ErrorCategory.API_ERROR:
            return api_error()
        if self is ErrorCategory.AUTHENTICATION_ERROR:
            return authentication_error()
        if self is ErrorCategory.INVALID_REQUEST_ERROR:
            return invalid_request_error()
        if self is ErrorCategory.RATE_LIMIT_ERROR:
            return rate_limit_error()
        if self is ErrorCategory.PAYMENT_METHOD_ERROR:
            return payment_method_error()
        if self is ErrorCategory.REFUND_ERROR:
            return refund_error()
        if self is ErrorCategory.MERCHANT_SUBSCRIPTION_ERROR:
            return merchant_subscription_error()
