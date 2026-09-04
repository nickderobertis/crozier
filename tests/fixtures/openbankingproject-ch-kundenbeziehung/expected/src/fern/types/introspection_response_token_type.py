

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IntrospectionResponseTokenType(enum.StrEnum):
    """
    Token type
    """

    BEARER = "Bearer"
    D_PO_P = "DPoP"

    def visit(self, bearer: typing.Callable[[], T_Result], d_po_p: typing.Callable[[], T_Result]) -> T_Result:
        if self is IntrospectionResponseTokenType.BEARER:
            return bearer()
        if self is IntrospectionResponseTokenType.D_PO_P:
            return d_po_p()
