

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCertsResponseKeysItemUse(enum.StrEnum):
    """
    How the Key is used. Valid value: sig
    """

    SIG = "sig"

    def visit(self, sig: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCertsResponseKeysItemUse.SIG:
            return sig()
