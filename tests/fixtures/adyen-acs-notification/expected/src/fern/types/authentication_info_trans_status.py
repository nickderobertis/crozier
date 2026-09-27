

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationInfoTransStatus(enum.StrEnum):
    """
    The `transStatus` value as defined in the 3D Secure 2 specification. Possible values:

    * **Y**: Authentication / Account verification successful.
    * **N**: Not Authenticated / Account not verified. Transaction denied.
    * **U**: Authentication / Account verification could not be performed.
    * **I**: Informational Only / 3D Secure Requestor challenge preference acknowledged.
    * **R**: Authentication / Account verification rejected by the Issuer.
    """

    Y = "Y"
    N = "N"
    R = "R"
    I = "I"
    U = "U"

    def visit(
        self,
        y: typing.Callable[[], T_Result],
        n: typing.Callable[[], T_Result],
        r: typing.Callable[[], T_Result],
        i: typing.Callable[[], T_Result],
        u: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthenticationInfoTransStatus.Y:
            return y()
        if self is AuthenticationInfoTransStatus.N:
            return n()
        if self is AuthenticationInfoTransStatus.R:
            return r()
        if self is AuthenticationInfoTransStatus.I:
            return i()
        if self is AuthenticationInfoTransStatus.U:
            return u()
