

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthFactorType(enum.StrEnum):
    """
    Name of the authentication method
    """

    PIN = "PIN"
    OTP = "OTP"
    L1BIO_DEVICE = "L1-bio-device"
    WALLET = "Wallet"
    KBI = "KBI"

    def visit(
        self,
        pin: typing.Callable[[], T_Result],
        otp: typing.Callable[[], T_Result],
        l1bio_device: typing.Callable[[], T_Result],
        wallet: typing.Callable[[], T_Result],
        kbi: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthFactorType.PIN:
            return pin()
        if self is AuthFactorType.OTP:
            return otp()
        if self is AuthFactorType.L1BIO_DEVICE:
            return l1bio_device()
        if self is AuthFactorType.WALLET:
            return wallet()
        if self is AuthFactorType.KBI:
            return kbi()
