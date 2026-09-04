

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchClientClientIdRequestRequestEncPublicKeyEe(enum.StrEnum):
    """
    RSA exponent
    """

    AQAB = "AQAB"

    def visit(self, aqab: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchClientClientIdRequestRequestEncPublicKeyEe.AQAB:
            return aqab()
