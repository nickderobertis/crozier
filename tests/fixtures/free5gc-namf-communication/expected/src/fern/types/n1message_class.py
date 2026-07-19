

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class N1MessageClass(enum.StrEnum):
    FIVE_GMM = "5GMM"
    SM = "SM"
    LPP = "LPP"
    SMS = "SMS"
    UPDP = "UPDP"

    def visit(
        self,
        five_gmm: typing.Callable[[], T_Result],
        sm: typing.Callable[[], T_Result],
        lpp: typing.Callable[[], T_Result],
        sms: typing.Callable[[], T_Result],
        updp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is N1MessageClass.FIVE_GMM:
            return five_gmm()
        if self is N1MessageClass.SM:
            return sm()
        if self is N1MessageClass.LPP:
            return lpp()
        if self is N1MessageClass.SMS:
            return sms()
        if self is N1MessageClass.UPDP:
            return updp()
