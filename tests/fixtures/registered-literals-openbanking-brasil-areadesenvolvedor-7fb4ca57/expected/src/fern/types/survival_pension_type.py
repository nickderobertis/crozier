

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurvivalPensionType(enum.StrEnum):
    """
    1.  PGBL
    2.  PRGP
    3.  PAGP
    4.  PRSA
    5.  PRI
    6.  PDR
    7.  VGBL
    8.  VRGP
    9.  VAGP
    10. VRSA
    11. VRI
    12. VDR
    13. Demais produtos de Previdência.
    """

    PGBL = "PGBL"
    PRGP = "PRGP"
    PAGP = "PAGP"
    PRSA = "PRSA"
    PRI = "PRI"
    PDR = "PDR"
    VGBL = "VGBL"
    VRGP = "VRGP"
    VAGP = "VAGP"
    VRSA = "VRSA"
    VRI = "VRI"
    VDR = "VDR"
    DEMAIS_PRODUTOS_PREVIDENCIA = "DEMAIS_PRODUTOS_PREVIDENCIA"

    def visit(
        self,
        pgbl: typing.Callable[[], T_Result],
        prgp: typing.Callable[[], T_Result],
        pagp: typing.Callable[[], T_Result],
        prsa: typing.Callable[[], T_Result],
        pri: typing.Callable[[], T_Result],
        pdr: typing.Callable[[], T_Result],
        vgbl: typing.Callable[[], T_Result],
        vrgp: typing.Callable[[], T_Result],
        vagp: typing.Callable[[], T_Result],
        vrsa: typing.Callable[[], T_Result],
        vri: typing.Callable[[], T_Result],
        vdr: typing.Callable[[], T_Result],
        demais_produtos_previdencia: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurvivalPensionType.PGBL:
            return pgbl()
        if self is SurvivalPensionType.PRGP:
            return prgp()
        if self is SurvivalPensionType.PAGP:
            return pagp()
        if self is SurvivalPensionType.PRSA:
            return prsa()
        if self is SurvivalPensionType.PRI:
            return pri()
        if self is SurvivalPensionType.PDR:
            return pdr()
        if self is SurvivalPensionType.VGBL:
            return vgbl()
        if self is SurvivalPensionType.VRGP:
            return vrgp()
        if self is SurvivalPensionType.VAGP:
            return vagp()
        if self is SurvivalPensionType.VRSA:
            return vrsa()
        if self is SurvivalPensionType.VRI:
            return vri()
        if self is SurvivalPensionType.VDR:
            return vdr()
        if self is SurvivalPensionType.DEMAIS_PRODUTOS_PREVIDENCIA:
            return demais_produtos_previdencia()
