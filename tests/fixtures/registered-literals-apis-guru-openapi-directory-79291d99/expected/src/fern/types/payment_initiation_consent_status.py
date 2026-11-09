

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentInitiationConsentStatus(enum.StrEnum):
    """
    The status of the payment consent.

    `UNAUTHORISED`: Consent created, but requires user authorisation.

    `REJECTED`: Consent authorisation was rejected by the user and/or the bank.

    `AUTHORISED`: Consent is active and ready to be used.

    `REVOKED`: Consent has been revoked and can no longer be used.

    `EXPIRED`: Consent is no longer valid.
    """

    UNAUTHORISED = "UNAUTHORISED"
    AUTHORISED = "AUTHORISED"
    REVOKED = "REVOKED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"

    def visit(
        self,
        unauthorised: typing.Callable[[], T_Result],
        authorised: typing.Callable[[], T_Result],
        revoked: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentInitiationConsentStatus.UNAUTHORISED:
            return unauthorised()
        if self is PaymentInitiationConsentStatus.AUTHORISED:
            return authorised()
        if self is PaymentInitiationConsentStatus.REVOKED:
            return revoked()
        if self is PaymentInitiationConsentStatus.REJECTED:
            return rejected()
        if self is PaymentInitiationConsentStatus.EXPIRED:
            return expired()
