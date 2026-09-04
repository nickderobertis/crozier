

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchClientClientIdRequestRequestEncPublicKeyCrvUse(enum.StrEnum):
    """
    Key use (enc for encryption)
    """

    ENC = "enc"

    def visit(self, enc: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchClientClientIdRequestRequestEncPublicKeyCrvUse.ENC:
            return enc()
