

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SmsSupport(enum.StrEnum):
    THREE_GPP = "3GPP"
    NON3GPP = "NON_3GPP"
    BOTH = "BOTH"
    NONE = "NONE"

    def visit(
        self,
        three_gpp: typing.Callable[[], T_Result],
        non3gpp: typing.Callable[[], T_Result],
        both: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SmsSupport.THREE_GPP:
            return three_gpp()
        if self is SmsSupport.NON3GPP:
            return non3gpp()
        if self is SmsSupport.BOTH:
            return both()
        if self is SmsSupport.NONE:
            return none()
