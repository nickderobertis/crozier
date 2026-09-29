

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchBySmartsRequestDb(enum.StrEnum):
    CALIBRATE = "calibrate"
    ENANOMAPPER = "enanomapper"
    ENPRA = "enpra"
    MARINA = "marina"
    NANOGENOTOX = "nanogenotox"
    NANOINFORMATIX = "nanoinformatix"
    NANOREG1 = "nanoreg1"
    NANOREG2 = "nanoreg2"
    NANOTEST = "nanotest"

    def visit(
        self,
        calibrate: typing.Callable[[], T_Result],
        enanomapper: typing.Callable[[], T_Result],
        enpra: typing.Callable[[], T_Result],
        marina: typing.Callable[[], T_Result],
        nanogenotox: typing.Callable[[], T_Result],
        nanoinformatix: typing.Callable[[], T_Result],
        nanoreg1: typing.Callable[[], T_Result],
        nanoreg2: typing.Callable[[], T_Result],
        nanotest: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchBySmartsRequestDb.CALIBRATE:
            return calibrate()
        if self is SearchBySmartsRequestDb.ENANOMAPPER:
            return enanomapper()
        if self is SearchBySmartsRequestDb.ENPRA:
            return enpra()
        if self is SearchBySmartsRequestDb.MARINA:
            return marina()
        if self is SearchBySmartsRequestDb.NANOGENOTOX:
            return nanogenotox()
        if self is SearchBySmartsRequestDb.NANOINFORMATIX:
            return nanoinformatix()
        if self is SearchBySmartsRequestDb.NANOREG1:
            return nanoreg1()
        if self is SearchBySmartsRequestDb.NANOREG2:
            return nanoreg2()
        if self is SearchBySmartsRequestDb.NANOTEST:
            return nanotest()
