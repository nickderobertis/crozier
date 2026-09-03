

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenResponseTokenType(enum.StrEnum):
    """
    Token type (Bearer or DPoP)
    """

    BEARER = "Bearer"
    D_PO_P = "DPoP"

    def visit(self, bearer: typing.Callable[[], T_Result], d_po_p: typing.Callable[[], T_Result]) -> T_Result:
        if self is TokenResponseTokenType.BEARER:
            return bearer()
        if self is TokenResponseTokenType.D_PO_P:
            return d_po_p()
