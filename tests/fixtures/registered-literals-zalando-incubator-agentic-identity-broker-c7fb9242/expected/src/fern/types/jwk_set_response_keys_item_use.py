

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JwkSetResponseKeysItemUse(enum.StrEnum):
    """
    Key usage (always "sig" for signing)
    """

    SIG = "sig"

    def visit(self, sig: typing.Callable[[], T_Result]) -> T_Result:
        if self is JwkSetResponseKeysItemUse.SIG:
            return sig()
