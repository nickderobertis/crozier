

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObFeeFrequency1Code3(enum.StrEnum):
    """
    How frequently the fee/charge is calculated
    """

    FEAC = "FEAC"
    FEAO = "FEAO"
    FECP = "FECP"
    FEDA = "FEDA"
    FEHO = "FEHO"
    FEI = "FEI"
    FEMO = "FEMO"
    FEOA = "FEOA"
    FEOT = "FEOT"
    FEPC = "FEPC"
    FEPH = "FEPH"
    FEPO = "FEPO"
    FEPS = "FEPS"
    FEPT = "FEPT"
    FEPTA = "FEPTA"
    FEPTP = "FEPTP"
    FEQU = "FEQU"
    FESM = "FESM"
    FEST = "FEST"
    FEWE = "FEWE"
    FEYE = "FEYE"

    def visit(
        self,
        feac: typing.Callable[[], T_Result],
        feao: typing.Callable[[], T_Result],
        fecp: typing.Callable[[], T_Result],
        feda: typing.Callable[[], T_Result],
        feho: typing.Callable[[], T_Result],
        fei: typing.Callable[[], T_Result],
        femo: typing.Callable[[], T_Result],
        feoa: typing.Callable[[], T_Result],
        feot: typing.Callable[[], T_Result],
        fepc: typing.Callable[[], T_Result],
        feph: typing.Callable[[], T_Result],
        fepo: typing.Callable[[], T_Result],
        feps: typing.Callable[[], T_Result],
        fept: typing.Callable[[], T_Result],
        fepta: typing.Callable[[], T_Result],
        feptp: typing.Callable[[], T_Result],
        fequ: typing.Callable[[], T_Result],
        fesm: typing.Callable[[], T_Result],
        fest: typing.Callable[[], T_Result],
        fewe: typing.Callable[[], T_Result],
        feye: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObFeeFrequency1Code3.FEAC:
            return feac()
        if self is ObFeeFrequency1Code3.FEAO:
            return feao()
        if self is ObFeeFrequency1Code3.FECP:
            return fecp()
        if self is ObFeeFrequency1Code3.FEDA:
            return feda()
        if self is ObFeeFrequency1Code3.FEHO:
            return feho()
        if self is ObFeeFrequency1Code3.FEI:
            return fei()
        if self is ObFeeFrequency1Code3.FEMO:
            return femo()
        if self is ObFeeFrequency1Code3.FEOA:
            return feoa()
        if self is ObFeeFrequency1Code3.FEOT:
            return feot()
        if self is ObFeeFrequency1Code3.FEPC:
            return fepc()
        if self is ObFeeFrequency1Code3.FEPH:
            return feph()
        if self is ObFeeFrequency1Code3.FEPO:
            return fepo()
        if self is ObFeeFrequency1Code3.FEPS:
            return feps()
        if self is ObFeeFrequency1Code3.FEPT:
            return fept()
        if self is ObFeeFrequency1Code3.FEPTA:
            return fepta()
        if self is ObFeeFrequency1Code3.FEPTP:
            return feptp()
        if self is ObFeeFrequency1Code3.FEQU:
            return fequ()
        if self is ObFeeFrequency1Code3.FESM:
            return fesm()
        if self is ObFeeFrequency1Code3.FEST:
            return fest()
        if self is ObFeeFrequency1Code3.FEWE:
            return fewe()
        if self is ObFeeFrequency1Code3.FEYE:
            return feye()
