

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JwkUse(enum.StrEnum):
    """
    Key use
    """

    SIG = "sig"
    ENC = "enc"

    def visit(self, sig: typing.Callable[[], T_Result], enc: typing.Callable[[], T_Result]) -> T_Result:
        if self is JwkUse.SIG:
            return sig()
        if self is JwkUse.ENC:
            return enc()
