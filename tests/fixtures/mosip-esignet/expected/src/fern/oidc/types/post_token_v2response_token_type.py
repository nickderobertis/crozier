

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostTokenV2ResponseTokenType(enum.StrEnum):
    """
    The type of the access token, set to either Bearer or DPoP
    """

    BEARER = "Bearer"
    D_PO_P = "DPoP"

    def visit(self, bearer: typing.Callable[[], T_Result], d_po_p: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostTokenV2ResponseTokenType.BEARER:
            return bearer()
        if self is PostTokenV2ResponseTokenType.D_PO_P:
            return d_po_p()
