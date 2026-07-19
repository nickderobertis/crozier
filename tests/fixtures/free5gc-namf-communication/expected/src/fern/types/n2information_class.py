

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class N2InformationClass(enum.StrEnum):
    SM = "SM"
    NRP_PA = "NRPPa"
    PWS = "PWS"
    PWS_BCAL = "PWS-BCAL"
    PWS_RF = "PWS-RF"
    RAN = "RAN"

    def visit(
        self,
        sm: typing.Callable[[], T_Result],
        nrp_pa: typing.Callable[[], T_Result],
        pws: typing.Callable[[], T_Result],
        pws_bcal: typing.Callable[[], T_Result],
        pws_rf: typing.Callable[[], T_Result],
        ran: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is N2InformationClass.SM:
            return sm()
        if self is N2InformationClass.NRP_PA:
            return nrp_pa()
        if self is N2InformationClass.PWS:
            return pws()
        if self is N2InformationClass.PWS_BCAL:
            return pws_bcal()
        if self is N2InformationClass.PWS_RF:
            return pws_rf()
        if self is N2InformationClass.RAN:
            return ran()
