

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WpMetadataDtoReadingProgression(enum.StrEnum):
    RTL = "rtl"
    LTR = "ltr"
    TTB = "ttb"
    BTT = "btt"
    AUTO = "auto"

    def visit(
        self,
        rtl: typing.Callable[[], T_Result],
        ltr: typing.Callable[[], T_Result],
        ttb: typing.Callable[[], T_Result],
        btt: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WpMetadataDtoReadingProgression.RTL:
            return rtl()
        if self is WpMetadataDtoReadingProgression.LTR:
            return ltr()
        if self is WpMetadataDtoReadingProgression.TTB:
            return ttb()
        if self is WpMetadataDtoReadingProgression.BTT:
            return btt()
        if self is WpMetadataDtoReadingProgression.AUTO:
            return auto()
