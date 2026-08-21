

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SslSupportMethod(enum.StrEnum):
    SNI_ONLY = "sni-only"
    VIP = "vip"

    def visit(self, sni_only: typing.Callable[[], T_Result], vip: typing.Callable[[], T_Result]) -> T_Result:
        if self is SslSupportMethod.SNI_ONLY:
            return sni_only()
        if self is SslSupportMethod.VIP:
            return vip()
