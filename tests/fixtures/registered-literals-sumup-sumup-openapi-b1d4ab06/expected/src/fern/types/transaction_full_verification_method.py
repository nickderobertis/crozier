

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionFullVerificationMethod(enum.StrEnum):
    """
    Verification method used for the transaction.
    """

    NONE = "none"
    SIGNATURE = "signature"
    OFFLINE_PIN = "offline PIN"
    ONLINE_PIN = "online PIN"
    OFFLINE_PIN_SIGNATURE = "offline PIN + signature"
    NA = "na"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        signature: typing.Callable[[], T_Result],
        offline_pin: typing.Callable[[], T_Result],
        online_pin: typing.Callable[[], T_Result],
        offline_pin_signature: typing.Callable[[], T_Result],
        na: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionFullVerificationMethod.NONE:
            return none()
        if self is TransactionFullVerificationMethod.SIGNATURE:
            return signature()
        if self is TransactionFullVerificationMethod.OFFLINE_PIN:
            return offline_pin()
        if self is TransactionFullVerificationMethod.ONLINE_PIN:
            return online_pin()
        if self is TransactionFullVerificationMethod.OFFLINE_PIN_SIGNATURE:
            return offline_pin_signature()
        if self is TransactionFullVerificationMethod.NA:
            return na()
