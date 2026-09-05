

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContactRoleEnum(enum.StrEnum):
    """
    The role of the contact
    """

    PTC = "PTC"
    STC = "STC"
    PBC = "PBC"
    SBC = "SBC"
    PSDC = "PSDC"
    SSDC = "SSDC"
    PDRC = "PDRC"
    SDRC = "SDRC"
    PPC = "PPC"
    SPC = "SPC"
    PCPC = "PCPC"
    SCPC = "SCPC"

    def visit(
        self,
        ptc: typing.Callable[[], T_Result],
        stc: typing.Callable[[], T_Result],
        pbc: typing.Callable[[], T_Result],
        sbc: typing.Callable[[], T_Result],
        psdc: typing.Callable[[], T_Result],
        ssdc: typing.Callable[[], T_Result],
        pdrc: typing.Callable[[], T_Result],
        sdrc: typing.Callable[[], T_Result],
        ppc: typing.Callable[[], T_Result],
        spc: typing.Callable[[], T_Result],
        pcpc: typing.Callable[[], T_Result],
        scpc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContactRoleEnum.PTC:
            return ptc()
        if self is ContactRoleEnum.STC:
            return stc()
        if self is ContactRoleEnum.PBC:
            return pbc()
        if self is ContactRoleEnum.SBC:
            return sbc()
        if self is ContactRoleEnum.PSDC:
            return psdc()
        if self is ContactRoleEnum.SSDC:
            return ssdc()
        if self is ContactRoleEnum.PDRC:
            return pdrc()
        if self is ContactRoleEnum.SDRC:
            return sdrc()
        if self is ContactRoleEnum.PPC:
            return ppc()
        if self is ContactRoleEnum.SPC:
            return spc()
        if self is ContactRoleEnum.PCPC:
            return pcpc()
        if self is ContactRoleEnum.SCPC:
            return scpc()
