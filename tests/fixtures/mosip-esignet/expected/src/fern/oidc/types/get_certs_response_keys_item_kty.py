

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCertsResponseKeysItemKty(enum.StrEnum):
    """
    Cryptographic algorithm family for the certificate's Key pair. Valid value: RSA
    """

    RSA = "RSA"

    def visit(self, rsa: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCertsResponseKeysItemKty.RSA:
            return rsa()
