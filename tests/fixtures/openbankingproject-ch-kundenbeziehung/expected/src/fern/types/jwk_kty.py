

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JwkKty(enum.StrEnum):
    """
    Key type
    """

    RSA = "RSA"
    EC = "EC"
    OKP = "OKP"

    def visit(
        self, rsa: typing.Callable[[], T_Result], ec: typing.Callable[[], T_Result], okp: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is JwkKty.RSA:
            return rsa()
        if self is JwkKty.EC:
            return ec()
        if self is JwkKty.OKP:
            return okp()
