

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchClientClientIdRequestRequestEncPublicKeyEKty(enum.StrEnum):
    """
    Key type (RSA)
    """

    RSA = "RSA"

    def visit(self, rsa: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchClientClientIdRequestRequestEncPublicKeyEKty.RSA:
            return rsa()
