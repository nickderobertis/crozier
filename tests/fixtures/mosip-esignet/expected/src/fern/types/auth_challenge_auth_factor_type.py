

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthChallengeAuthFactorType(enum.StrEnum):
    """
    Defines the type of auth challenge. It should be same as authfactor.type (oauth-details response).
    """

    OTP = "OTP"
    BIO = "BIO"
    PIN = "PIN"
    WLA = "WLA"
    PWD = "PWD"
    KBI = "KBI"
    IDT = "IDT"

    def visit(
        self,
        otp: typing.Callable[[], T_Result],
        bio: typing.Callable[[], T_Result],
        pin: typing.Callable[[], T_Result],
        wla: typing.Callable[[], T_Result],
        pwd: typing.Callable[[], T_Result],
        kbi: typing.Callable[[], T_Result],
        idt: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthChallengeAuthFactorType.OTP:
            return otp()
        if self is AuthChallengeAuthFactorType.BIO:
            return bio()
        if self is AuthChallengeAuthFactorType.PIN:
            return pin()
        if self is AuthChallengeAuthFactorType.WLA:
            return wla()
        if self is AuthChallengeAuthFactorType.PWD:
            return pwd()
        if self is AuthChallengeAuthFactorType.KBI:
            return kbi()
        if self is AuthChallengeAuthFactorType.IDT:
            return idt()
