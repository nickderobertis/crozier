

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchClientClientIdRequestRequestEncPublicKeyEAlg(enum.StrEnum):
    """
    Algorithm for key management
    """

    RSA_OAEP256 = "RSA-OAEP-256"
    RSA_OAEP = "RSA-OAEP"

    def visit(self, rsa_oaep256: typing.Callable[[], T_Result], rsa_oaep: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchClientClientIdRequestRequestEncPublicKeyEAlg.RSA_OAEP256:
            return rsa_oaep256()
        if self is PatchClientClientIdRequestRequestEncPublicKeyEAlg.RSA_OAEP:
            return rsa_oaep()
