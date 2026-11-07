

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentStatusReason(enum.StrEnum):
    """
    The reason for the payment's status.
    """

    OTHER = "OTHER"
    APPROVED = "APPROVED"
    EXCEEDED_BUDGET_LIMIT = "EXCEEDED_BUDGET_LIMIT"
    BUDGET_EXPIRED = "BUDGET_EXPIRED"
    NO_BUDGET = "NO_BUDGET"
    BUDGET_NOT_YET_STARTED = "BUDGET_NOT_YET_STARTED"
    BUDGET_CATEGORY_RESTRICTION = "BUDGET_CATEGORY_RESTRICTION"
    BUDGET_MERCHANT_RESTRICTION = "BUDGET_MERCHANT_RESTRICTION"
    SUSPECTED_FRAUD = "SUSPECTED_FRAUD"
    EXCEEDED_GLOBAL_LIMIT = "EXCEEDED_GLOBAL_LIMIT"
    EXCEEDED_USER_LIMIT = "EXCEEDED_USER_LIMIT"
    EXCEEDED_CARD_LIMIT = "EXCEEDED_CARD_LIMIT"
    INVALID_EXPIRATION_DATE = "INVALID_EXPIRATION_DATE"
    CARD_NOT_ACTIVE = "CARD_NOT_ACTIVE"
    INVALID_CARD_CREDENTIALS = "INVALID_CARD_CREDENTIALS"
    INVALID_BILLING_ADDRESS = "INVALID_BILLING_ADDRESS"
    CARD_SUSPENDED = "CARD_SUSPENDED"
    CARD_TERMINATED = "CARD_TERMINATED"
    CARD_EXPIRED = "CARD_EXPIRED"
    MCC_BLOCKED = "MCC_BLOCKED"
    USER_SUSPENDED = "USER_SUSPENDED"
    INVALID_PIN = "INVALID_PIN"
    INVALID_CVV = "INVALID_CVV"
    EXCEEDED_PIN_ATTEMPTS = "EXCEEDED_PIN_ATTEMPTS"
    INSIDE_SANCTIONED_COUNTRY = "INSIDE_SANCTIONED_COUNTRY"
    SOFT_EXPIRATION = "SOFT_EXPIRATION"
    TRANSFERRED_CARD_NEW_MERCHANT = "TRANSFERRED_CARD_NEW_MERCHANT"
    EXCEEDED_ANCESTOR_BUDGET_LIMIT = "EXCEEDED_ANCESTOR_BUDGET_LIMIT"
    EXCEEDED_BUDGET_TRANSACTION_LIMIT = "EXCEEDED_BUDGET_TRANSACTION_LIMIT"
    TOS_BLOCKED = "TOS_BLOCKED"
    COMPLIANCE_BLOCKED = "COMPLIANCE_BLOCKED"

    def visit(
        self,
        other: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        exceeded_budget_limit: typing.Callable[[], T_Result],
        budget_expired: typing.Callable[[], T_Result],
        no_budget: typing.Callable[[], T_Result],
        budget_not_yet_started: typing.Callable[[], T_Result],
        budget_category_restriction: typing.Callable[[], T_Result],
        budget_merchant_restriction: typing.Callable[[], T_Result],
        suspected_fraud: typing.Callable[[], T_Result],
        exceeded_global_limit: typing.Callable[[], T_Result],
        exceeded_user_limit: typing.Callable[[], T_Result],
        exceeded_card_limit: typing.Callable[[], T_Result],
        invalid_expiration_date: typing.Callable[[], T_Result],
        card_not_active: typing.Callable[[], T_Result],
        invalid_card_credentials: typing.Callable[[], T_Result],
        invalid_billing_address: typing.Callable[[], T_Result],
        card_suspended: typing.Callable[[], T_Result],
        card_terminated: typing.Callable[[], T_Result],
        card_expired: typing.Callable[[], T_Result],
        mcc_blocked: typing.Callable[[], T_Result],
        user_suspended: typing.Callable[[], T_Result],
        invalid_pin: typing.Callable[[], T_Result],
        invalid_cvv: typing.Callable[[], T_Result],
        exceeded_pin_attempts: typing.Callable[[], T_Result],
        inside_sanctioned_country: typing.Callable[[], T_Result],
        soft_expiration: typing.Callable[[], T_Result],
        transferred_card_new_merchant: typing.Callable[[], T_Result],
        exceeded_ancestor_budget_limit: typing.Callable[[], T_Result],
        exceeded_budget_transaction_limit: typing.Callable[[], T_Result],
        tos_blocked: typing.Callable[[], T_Result],
        compliance_blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentStatusReason.OTHER:
            return other()
        if self is PaymentStatusReason.APPROVED:
            return approved()
        if self is PaymentStatusReason.EXCEEDED_BUDGET_LIMIT:
            return exceeded_budget_limit()
        if self is PaymentStatusReason.BUDGET_EXPIRED:
            return budget_expired()
        if self is PaymentStatusReason.NO_BUDGET:
            return no_budget()
        if self is PaymentStatusReason.BUDGET_NOT_YET_STARTED:
            return budget_not_yet_started()
        if self is PaymentStatusReason.BUDGET_CATEGORY_RESTRICTION:
            return budget_category_restriction()
        if self is PaymentStatusReason.BUDGET_MERCHANT_RESTRICTION:
            return budget_merchant_restriction()
        if self is PaymentStatusReason.SUSPECTED_FRAUD:
            return suspected_fraud()
        if self is PaymentStatusReason.EXCEEDED_GLOBAL_LIMIT:
            return exceeded_global_limit()
        if self is PaymentStatusReason.EXCEEDED_USER_LIMIT:
            return exceeded_user_limit()
        if self is PaymentStatusReason.EXCEEDED_CARD_LIMIT:
            return exceeded_card_limit()
        if self is PaymentStatusReason.INVALID_EXPIRATION_DATE:
            return invalid_expiration_date()
        if self is PaymentStatusReason.CARD_NOT_ACTIVE:
            return card_not_active()
        if self is PaymentStatusReason.INVALID_CARD_CREDENTIALS:
            return invalid_card_credentials()
        if self is PaymentStatusReason.INVALID_BILLING_ADDRESS:
            return invalid_billing_address()
        if self is PaymentStatusReason.CARD_SUSPENDED:
            return card_suspended()
        if self is PaymentStatusReason.CARD_TERMINATED:
            return card_terminated()
        if self is PaymentStatusReason.CARD_EXPIRED:
            return card_expired()
        if self is PaymentStatusReason.MCC_BLOCKED:
            return mcc_blocked()
        if self is PaymentStatusReason.USER_SUSPENDED:
            return user_suspended()
        if self is PaymentStatusReason.INVALID_PIN:
            return invalid_pin()
        if self is PaymentStatusReason.INVALID_CVV:
            return invalid_cvv()
        if self is PaymentStatusReason.EXCEEDED_PIN_ATTEMPTS:
            return exceeded_pin_attempts()
        if self is PaymentStatusReason.INSIDE_SANCTIONED_COUNTRY:
            return inside_sanctioned_country()
        if self is PaymentStatusReason.SOFT_EXPIRATION:
            return soft_expiration()
        if self is PaymentStatusReason.TRANSFERRED_CARD_NEW_MERCHANT:
            return transferred_card_new_merchant()
        if self is PaymentStatusReason.EXCEEDED_ANCESTOR_BUDGET_LIMIT:
            return exceeded_ancestor_budget_limit()
        if self is PaymentStatusReason.EXCEEDED_BUDGET_TRANSACTION_LIMIT:
            return exceeded_budget_transaction_limit()
        if self is PaymentStatusReason.TOS_BLOCKED:
            return tos_blocked()
        if self is PaymentStatusReason.COMPLIANCE_BLOCKED:
            return compliance_blocked()
