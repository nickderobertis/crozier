

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchByIdentifierRequestDb(enum.StrEnum):
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
        if self is SearchByIdentifierRequestDb.CALIBRATE:
            return calibrate()
        if self is SearchByIdentifierRequestDb.ENANOMAPPER:
            return enanomapper()
        if self is SearchByIdentifierRequestDb.ENPRA:
            return enpra()
        if self is SearchByIdentifierRequestDb.MARINA:
            return marina()
        if self is SearchByIdentifierRequestDb.NANOGENOTOX:
            return nanogenotox()
        if self is SearchByIdentifierRequestDb.NANOINFORMATIX:
            return nanoinformatix()
        if self is SearchByIdentifierRequestDb.NANOREG1:
            return nanoreg1()
        if self is SearchByIdentifierRequestDb.NANOREG2:
            return nanoreg2()
        if self is SearchByIdentifierRequestDb.NANOTEST:
            return nanotest()
