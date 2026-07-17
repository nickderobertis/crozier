

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableCableType(enum.StrEnum):
    CAT3 = "cat3"
    CAT5 = "cat5"
    CAT5E = "cat5e"
    CAT6 = "cat6"
    CAT6A = "cat6a"
    CAT7 = "cat7"
    CAT7A = "cat7a"
    CAT8 = "cat8"
    DAC_ACTIVE = "dac-active"
    DAC_PASSIVE = "dac-passive"
    MRJ21TRUNK = "mrj21-trunk"
    COAXIAL = "coaxial"
    MMF = "mmf"
    MMF_OM1 = "mmf-om1"
    MMF_OM2 = "mmf-om2"
    MMF_OM3 = "mmf-om3"
    MMF_OM4 = "mmf-om4"
    MMF_OM5 = "mmf-om5"
    SMF = "smf"
    SMF_OS1 = "smf-os1"
    SMF_OS2 = "smf-os2"
    AOC = "aoc"
    POWER = "power"

    def visit(
        self,
        cat3: typing.Callable[[], T_Result],
        cat5: typing.Callable[[], T_Result],
        cat5e: typing.Callable[[], T_Result],
        cat6: typing.Callable[[], T_Result],
        cat6a: typing.Callable[[], T_Result],
        cat7: typing.Callable[[], T_Result],
        cat7a: typing.Callable[[], T_Result],
        cat8: typing.Callable[[], T_Result],
        dac_active: typing.Callable[[], T_Result],
        dac_passive: typing.Callable[[], T_Result],
        mrj21trunk: typing.Callable[[], T_Result],
        coaxial: typing.Callable[[], T_Result],
        mmf: typing.Callable[[], T_Result],
        mmf_om1: typing.Callable[[], T_Result],
        mmf_om2: typing.Callable[[], T_Result],
        mmf_om3: typing.Callable[[], T_Result],
        mmf_om4: typing.Callable[[], T_Result],
        mmf_om5: typing.Callable[[], T_Result],
        smf: typing.Callable[[], T_Result],
        smf_os1: typing.Callable[[], T_Result],
        smf_os2: typing.Callable[[], T_Result],
        aoc: typing.Callable[[], T_Result],
        power: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableCableType.CAT3:
            return cat3()
        if self is WritableCableType.CAT5:
            return cat5()
        if self is WritableCableType.CAT5E:
            return cat5e()
        if self is WritableCableType.CAT6:
            return cat6()
        if self is WritableCableType.CAT6A:
            return cat6a()
        if self is WritableCableType.CAT7:
            return cat7()
        if self is WritableCableType.CAT7A:
            return cat7a()
        if self is WritableCableType.CAT8:
            return cat8()
        if self is WritableCableType.DAC_ACTIVE:
            return dac_active()
        if self is WritableCableType.DAC_PASSIVE:
            return dac_passive()
        if self is WritableCableType.MRJ21TRUNK:
            return mrj21trunk()
        if self is WritableCableType.COAXIAL:
            return coaxial()
        if self is WritableCableType.MMF:
            return mmf()
        if self is WritableCableType.MMF_OM1:
            return mmf_om1()
        if self is WritableCableType.MMF_OM2:
            return mmf_om2()
        if self is WritableCableType.MMF_OM3:
            return mmf_om3()
        if self is WritableCableType.MMF_OM4:
            return mmf_om4()
        if self is WritableCableType.MMF_OM5:
            return mmf_om5()
        if self is WritableCableType.SMF:
            return smf()
        if self is WritableCableType.SMF_OS1:
            return smf_os1()
        if self is WritableCableType.SMF_OS2:
            return smf_os2()
        if self is WritableCableType.AOC:
            return aoc()
        if self is WritableCableType.POWER:
            return power()
