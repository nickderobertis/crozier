

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CardTypeType(enum.StrEnum):
    EGK = "EGK"
    HBA_Q_SIG = "HBA_Q_SIG"
    HBA = "HBA"
    SMC_B = "SMC_B"
    HSM_B = "HSM_B"
    SMC_KT = "SMC_KT"
    KVK = "KVK"
    ZOD20 = "ZOD_2_0"
    UNKNOWN = "UNKNOWN"
    HB_AX = "HB_AX"
    SM_B = "SM_B"

    def visit(
        self,
        egk: typing.Callable[[], T_Result],
        hba_q_sig: typing.Callable[[], T_Result],
        hba: typing.Callable[[], T_Result],
        smc_b: typing.Callable[[], T_Result],
        hsm_b: typing.Callable[[], T_Result],
        smc_kt: typing.Callable[[], T_Result],
        kvk: typing.Callable[[], T_Result],
        zod20: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        hb_ax: typing.Callable[[], T_Result],
        sm_b: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CardTypeType.EGK:
            return egk()
        if self is CardTypeType.HBA_Q_SIG:
            return hba_q_sig()
        if self is CardTypeType.HBA:
            return hba()
        if self is CardTypeType.SMC_B:
            return smc_b()
        if self is CardTypeType.HSM_B:
            return hsm_b()
        if self is CardTypeType.SMC_KT:
            return smc_kt()
        if self is CardTypeType.KVK:
            return kvk()
        if self is CardTypeType.ZOD20:
            return zod20()
        if self is CardTypeType.UNKNOWN:
            return unknown()
        if self is CardTypeType.HB_AX:
            return hb_ax()
        if self is CardTypeType.SM_B:
            return sm_b()
