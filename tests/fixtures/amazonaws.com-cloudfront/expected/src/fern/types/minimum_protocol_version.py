

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MinimumProtocolVersion(enum.StrEnum):
    SS_LV3 = "SSLv3"
    TL_SV1 = "TLSv1"

    def visit(self, ss_lv3: typing.Callable[[], T_Result], tl_sv1: typing.Callable[[], T_Result]) -> T_Result:
        if self is MinimumProtocolVersion.SS_LV3:
            return ss_lv3()
        if self is MinimumProtocolVersion.TL_SV1:
            return tl_sv1()
