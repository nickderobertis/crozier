

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SslProtocolsListItem(enum.StrEnum):
    SS_LV3 = "SSLv3"
    TL_SV1 = "TLSv1"
    TL_SV11 = "TLSv1.1"
    TL_SV12 = "TLSv1.2"

    def visit(
        self,
        ss_lv3: typing.Callable[[], T_Result],
        tl_sv1: typing.Callable[[], T_Result],
        tl_sv11: typing.Callable[[], T_Result],
        tl_sv12: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SslProtocolsListItem.SS_LV3:
            return ss_lv3()
        if self is SslProtocolsListItem.TL_SV1:
            return tl_sv1()
        if self is SslProtocolsListItem.TL_SV11:
            return tl_sv11()
        if self is SslProtocolsListItem.TL_SV12:
            return tl_sv12()
