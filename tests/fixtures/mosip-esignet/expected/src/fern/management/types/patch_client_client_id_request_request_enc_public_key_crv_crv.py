

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchClientClientIdRequestRequestEncPublicKeyCrvCrv(enum.StrEnum):
    """
    Curve name
    """

    P256 = "P-256"
    P384 = "P-384"
    P521 = "P-521"

    def visit(
        self,
        p256: typing.Callable[[], T_Result],
        p384: typing.Callable[[], T_Result],
        p521: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchClientClientIdRequestRequestEncPublicKeyCrvCrv.P256:
            return p256()
        if self is PatchClientClientIdRequestRequestEncPublicKeyCrvCrv.P384:
            return p384()
        if self is PatchClientClientIdRequestRequestEncPublicKeyCrvCrv.P521:
            return p521()
