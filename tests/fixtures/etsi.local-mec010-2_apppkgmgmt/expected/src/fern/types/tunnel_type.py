

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TunnelType(enum.StrEnum):
    """
    Type of tunnel.
    """

    GTP_U = "GTP-U"
    GRE = "GRE"

    def visit(self, gtp_u: typing.Callable[[], T_Result], gre: typing.Callable[[], T_Result]) -> T_Result:
        if self is TunnelType.GTP_U:
            return gtp_u()
        if self is TunnelType.GRE:
            return gre()
